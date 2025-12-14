# 🚀 APIBlueprint Pro - Run Guide

Follow these instructions to run the full Hybrid Runtime (Backend + Frontend).

## 1️⃣ Prerequisites
- Python 3.10+
- Node.js 18+
- Dependencies installed:
  ```powershell
  pip install requests requests-mock pytest
  cd vercel-ui
  npm install
  cd ..
  ```

## 2️⃣ Start the Backend (API Wrapper)
This server acts as the bridge between the UI and the Python agent.

**Terminal 1:**
```powershell
# From the project root (api-blueprint-pro)
python api_server.py
```
✅ *Server will start on `http://localhost:8000`*

## 3️⃣ Start the Frontend (Vercel UI)
This is the Next.js dashboard.

**Terminal 2:**
```powershell
# From the project root
cd vercel-ui
npm run dev
```
✅ *UI will start on `http://localhost:3000`*

## 4️⃣ How to Use
1. Open `http://localhost:3000` in your browser.
2. Toggle between **URL** or **Text** mode.
3. Paste standard API documentation (or use the sample content below).
4. Click **Generate Python SDK**.
5. View the generated reports, error patterns, and repair logs instantly.

### 📝 Sample Input (Text Mode)
You can paste the content of `samples/vehicle_doc.md` to test it out:

```markdown
# Vehicle Alert API
POST /vehicles/alert
Creates an alert for a vehicle.
Body:
- voltage
- engine_temp
Responses:
- 200 OK
- 400 Bad Request
- 429 Too Many Requests
- 500 Server Error
```

## 5️⃣ Manual CLI Usage (Optional)
You can also run the agent directly without the UI:

```powershell
python -m api_blueprint.cli agent --input samples/vehicle_doc.md --out generated/my_run
```
