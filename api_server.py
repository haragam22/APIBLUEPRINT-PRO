import http.server
import socketserver
import json
import subprocess
import os
import requests

PORT = 8001




def detect_doc_type(raw_text, content_type):
    # OpenAPI JSON
    if "application/json" in content_type:
        try:
            data = json.loads(raw_text)
            if "openapi" in data or "swagger" in data or "paths" in data:
                return "openapi_json", data
        except:
            pass

    # OpenAPI YAML
    if "yaml" in content_type or raw_text.strip().startswith(("openapi:", "swagger:")):
        return "openapi_yaml", raw_text

    # HTML docs
    if "<html" in raw_text.lower():
        return "html", raw_text

    # Markdown docs
    if "```" in raw_text or raw_text.lstrip().startswith("#"):
        return "markdown", raw_text

    # Fallback
    return "text", raw_text

class AgentHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/run-agent':
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                data = json.loads(post_data)
                
                input_type = data.get('input_type')
                input_value = data.get('input_value')
                
                # Fetch content if URL
                raw_content = input_value
                content_type = "text/plain"
                
                if input_type == 'url':
                    print(f"Fetching URL: {input_value}")
                    resp = requests.get(input_value, timeout=10)
                    resp.raise_for_status()
                    raw_content = resp.text
                    content_type = resp.headers.get("Content-Type", "")

                # Detect Type
                doc_type, content = detect_doc_type(raw_content, content_type)
                print(f"🔍 Detected Document Type: {doc_type}")
                print("DOC TYPE DETECTED:", doc_type)

                # Route
                if doc_type.startswith("openapi"):
                    result = self.run_agent_from_openapi(content)
                else:
                    result = self.run_agent_from_text(content)
                    
                self._send_response(200, result)

            except Exception as e:
                import traceback
                traceback.print_exc()
                self._send_response(500, {'error': str(e)})
        else:
            self.send_error(404)

    def run_agent_from_openapi(self, content):
        # Wrapper: Ensure content is string format for the CLI agent
        if isinstance(content, dict):
            file_content = json.dumps(content)
        else:
            file_content = content
        return self._run_agent_subprocess(file_content)

    def run_agent_from_text(self, content):
        return self._run_agent_subprocess(content)

    def _run_agent_subprocess(self, file_content):
        # Save to temp file
        temp_input = "temp_input.md"
        with open(temp_input, "w", encoding='utf-8') as f:
            f.write(file_content)
            
        # Run Agent
        out_dir = "generated/hybrid_run"
        subprocess.run(
            ["python", "-m", "api_blueprint.cli", "agent", "--input", temp_input, "--out", out_dir],
            check=True
        )
        
        # Read Report
        report_path = os.path.join(out_dir, "report.json")
        if os.path.exists(report_path):
            with open(report_path, encoding='utf-8') as f:
                return json.load(f)
        else:
            raise Exception("Agent ran but produced no report")

    def _send_response(self, code, data):
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
        
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

if __name__ == "__main__":
    print(f"🚀 API Server running on port {PORT}")
    with socketserver.TCPServer(("", PORT), AgentHandler) as httpd:
        httpd.serve_forever()
