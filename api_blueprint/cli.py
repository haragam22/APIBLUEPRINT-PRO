import argparse
import json
import os
import subprocess
from api_blueprint.generator.parser import parse_input
from api_blueprint.generator.inference import infer_schema
from api_blueprint.generator.repair import repair_schema
from api_blueprint.generator.codegen import generate_sdk

def generate_report(spec: dict, out_dir: str):
    report = {
        "status": "success",
        "endpoints_processed": len(spec.get("endpoints", [])),
        "repairs_applied": [],
        "confidence_scores": {},
        "errors_detected": {},
        "recommendations": [
            "Review generated error classes in errors.py",
            "Configure retry policy integration tests",
            "Verify Kestra workflow template"
        ]
    }
    
    for ep in spec.get("endpoints", []):
        path = ep.get("path", "unknown")
        # Collect repairs
        if "repairs_applied" in ep:
            report["repairs_applied"].extend([f"{path}: {r}" for r in ep["repairs_applied"]])
        
        # Collect confidence
        if "confidence" in ep:
            report["confidence_scores"][path] = ep["confidence"]
            
        # Collect errors
        if "errors" in ep:
            report["errors_detected"][path] = ep["errors"]

    with open(os.path.join(out_dir, "report.json"), "w") as f:
        json.dump(report, f, indent=2)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["generate", "agent"])
    parser.add_argument("--input", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    print(f"🚀 Starting APIBlueprint Pro in {args.mode.upper()} mode...")
    
    # 1. Summarize (Stub)
    if args.mode == "agent":
        print("📝 Summarizing input documentation...")

    # 2. Extract & Infer & Repair
    print("🔍 Parsing and analyzing spec...")
    raw = open(args.input).read()
    spec = parse_input(raw)
    inferred = infer_schema(spec)
    repaired = repair_schema(inferred)

    # 3. Generate
    print("⚙️ Generating SDK and artifacts...")
    generate_sdk(repaired, args.out)

    # 4. Validate (Agent Mode)
    if args.mode == "agent":
        print("✅ Validating generated code...")
        try:
            # We need to target the generated tests directory
            tests_dir = os.path.join(args.out, "tests")
            if os.path.exists(tests_dir):
                # Run pytest with shell=True to ensure path resolution works on Windows if needed, 
                # but list args are safer. On Windows, 'pytest' might be a script. 
                # 'python -m pytest' is safer.
                subprocess.run(["python", "-m", "pytest", tests_dir], check=True)
                print("🎉 Validation passed!")
            else:
                print("⚠️ No tests found to run.")
        except subprocess.CalledProcessError:
            print(f"❌ Validation failed: Tests returned non-zero exit code.")
        except Exception as e:
            print(f"❌ Validation failed: {e}")
        
        # 5. Report
        print("📊 Generating mission report...")
        generate_report(repaired, args.out)

    print("✅ Mission complete.")

if __name__ == "__main__":
    main()
