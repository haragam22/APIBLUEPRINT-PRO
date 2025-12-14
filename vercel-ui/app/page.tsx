"use client";

import React, { useState } from 'react';
import { Play, FileText, Globe, CheckCircle, AlertTriangle, ShieldCheck, Download, Code, Terminal } from 'lucide-react';

export default function Home() {
  const [inputType, setInputType] = useState<'url' | 'text'>('url');
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [report, setReport] = useState<any>(null);

  const handleRun = async () => {
    setIsLoading(true);
    setReport(null);
    try {
      const res = await fetch('http://localhost:8001/run-agent', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ input_type: inputType, input_value: inputValue })
      });
      const data = await res.json();
      if (res.ok) {
        setReport(data);
      } else {
        alert("Error: " + data.error);
      }
    } catch (e) {
      alert("Failed to connect to Local Python Agent. Ensure api_server.py is running!");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-neutral-950 text-neutral-100 font-sans p-8">
      <div className="max-w-4xl mx-auto space-y-8">

        {/* Header */}
        <div className="flex items-center space-x-3 mb-8 border-b border-neutral-800 pb-6">
          <div className="p-3 bg-blue-600 rounded-lg shadow-lg shadow-blue-500/20">
            <Terminal className="w-6 h-6 text-white" />
          </div>
          <div>
            <h1 className="text-2xl font-bold tracking-tight text-white">APIBlueprint Pro</h1>
            <p className="text-neutral-400">Autonomous API SDK Engine</p>
          </div>
          <div className="ml-auto flex items-center space-x-2 text-xs font-mono text-neutral-500 bg-neutral-900 px-3 py-1 rounded-full border border-neutral-800">
            <span className="w-2 h-2 rounded-full bg-green-500 animate-pulse"></span>
            <span>AGENT: ONLINE</span>
          </div>
        </div>

        {/* Input Section */}
        <div className="bg-neutral-900/50 border border-neutral-800 rounded-xl p-6 backdrop-blur-sm">
          <div className="flex items-center space-x-6 mb-6">
            <label className={`flex items-center space-x-2 cursor-pointer transition-colors ${inputType === 'url' ? 'text-blue-400' : 'text-neutral-500'}`}>
              <input
                type="radio"
                name="inputType"
                value="url"
                checked={inputType === 'url'}
                onChange={() => setInputType('url')}
                className="hidden"
              />
              <Globe className="w-4 h-4" />
              <span className="font-medium">URL Mode</span>
              {inputType === 'url' && <div className="h-1.5 w-1.5 rounded-full bg-blue-500 ml-2" />}
            </label>

            <label className={`flex items-center space-x-2 cursor-pointer transition-colors ${inputType === 'text' ? 'text-blue-400' : 'text-neutral-500'}`}>
              <input
                type="radio"
                name="inputType"
                value="text"
                checked={inputType === 'text'}
                onChange={() => setInputType('text')}
                className="hidden"
              />
              <FileText className="w-4 h-4" />
              <span className="font-medium">Text Mode</span>
              {inputType === 'text' && <div className="h-1.5 w-1.5 rounded-full bg-blue-500 ml-2" />}
            </label>
          </div>

          <div className="space-y-4">
            {inputType === 'url' ? (
              <input
                type="text"
                placeholder="https://api.example.com/docs"
                className="w-full bg-neutral-950 border border-neutral-800 rounded-lg p-4 text-neutral-200 outline-none focus:ring-2 focus:ring-blue-500/50 transition-all font-mono text-sm"
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
              />
            ) : (
              <textarea
                placeholder="Paste raw API documentation here..."
                className="w-full bg-neutral-950 border border-neutral-800 rounded-lg p-4 text-neutral-200 outline-none focus:ring-2 focus:ring-blue-500/50 min-h-[150px] transition-all font-mono text-sm resize-y"
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
              />
            )}

            <button
              onClick={handleRun}
              disabled={isLoading || !inputValue}
              className={`w-full py-4 rounded-lg font-bold flex items-center justify-center space-x-2 transition-all transform active:scale-[0.99]
                ${isLoading || !inputValue
                  ? 'bg-neutral-800 text-neutral-500 cursor-not-allowed'
                  : 'bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white shadow-lg shadow-blue-500/20'}`}
            >
              {isLoading ? (
                <>
                  <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white"></div>
                  <span>Processing...</span>
                </>
              ) : (
                <>
                  <Play className="w-5 h-5 fill-current" />
                  <span>Generate Python SDK</span>
                </>
              )}
            </button>
          </div>
        </div>

        {/* Results Section */}
        {report && (
          <div className="space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-500">

            {/* Status Cards */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div className="bg-neutral-900/50 border border-neutral-800 p-5 rounded-xl flex flex-col items-center justify-center text-center">
                <div className="w-10 h-10 rounded-full bg-green-500/10 flex items-center justify-center mb-3 text-green-500">
                  <CheckCircle className="w-5 h-5" />
                </div>
                <div className="text-2xl font-bold text-white mb-1">{report.endpoints_processed}</div>
                <div className="text-xs text-neutral-500 uppercase tracking-wider font-semibold">Endpoints Detected</div>
              </div>

              <div className="bg-neutral-900/50 border border-neutral-800 p-5 rounded-xl flex flex-col items-center justify-center text-center">
                <div className="w-10 h-10 rounded-full bg-yellow-500/10 flex items-center justify-center mb-3 text-yellow-500">
                  <ShieldCheck className="w-5 h-5" />
                </div>
                <div className="text-2xl font-bold text-white mb-1">{report.repairs_applied.length}</div>
                <div className="text-xs text-neutral-500 uppercase tracking-wider font-semibold">Repairs Applied</div>
              </div>

              <div className="bg-neutral-900/50 border border-neutral-800 p-5 rounded-xl flex flex-col items-center justify-center text-center">
                <div className="w-10 h-10 rounded-full bg-red-500/10 flex items-center justify-center mb-3 text-red-500">
                  <AlertTriangle className="w-5 h-5" />
                </div>
                <div className="text-2xl font-bold text-white mb-1">{Object.keys(report.errors_detected).length}</div>
                <div className="text-xs text-neutral-500 uppercase tracking-wider font-semibold">Error Patterns</div>
              </div>
            </div>

            {/* Detailed Report Grid */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">

              {/* Repairs Log */}
              <div className="bg-neutral-900 border border-neutral-800 rounded-xl overflow-hidden flex flex-col">
                <div className="bg-neutral-800/50 px-6 py-3 border-b border-neutral-800 flex items-center font-medium text-sm">
                  <Code className="w-4 h-4 mr-2 text-blue-400" />
                  Repairs Log
                </div>
                <div className="p-4 space-y-2 text-sm font-mono text-neutral-400 max-h-[250px] overflow-y-auto">
                  {report.repairs_applied.map((r: string, i: number) => (
                    <div key={i} className="flex items-start space-x-2 p-2 rounded hover:bg-neutral-800/50 transition-colors">
                      <span className="text-green-500 mt-0.5">✓</span>
                      <span>{r}</span>
                    </div>
                  ))}
                  {report.repairs_applied.length === 0 && (
                    <div className="text-neutral-600 italic p-2">No repairs needed.</div>
                  )}
                </div>
              </div>

              {/* Recommendations */}
              <div className="bg-neutral-900 border border-neutral-800 rounded-xl overflow-hidden flex flex-col">
                <div className="bg-neutral-800/50 px-6 py-3 border-b border-neutral-800 flex items-center font-medium text-sm">
                  <CheckCircle className="w-4 h-4 mr-2 text-blue-400" />
                  Agent Recommendations
                </div>
                <div className="p-4 space-y-2 text-sm text-neutral-400 max-h-[250px] overflow-y-auto">
                  {report.recommendations.map((rec: string, i: number) => (
                    <div key={i} className="flex items-center space-x-3 p-2 rounded hover:bg-neutral-800/50 transition-colors border border-transparent hover:border-neutral-800">
                      <div className="h-1.5 w-1.5 rounded-full bg-blue-500"></div>
                      <span>{rec}</span>
                    </div>
                  ))}
                </div>
              </div>

            </div>

            {/* Download / Success Action */}
            <div className="flex justify-center pt-4">
              <button className="flex items-center space-x-2 text-green-400 hover:text-green-300 transition-colors font-medium border border-green-500/20 hover:border-green-500/40 bg-green-500/5 px-6 py-3 rounded-full">
                <Download className="w-5 h-5" />
                <span>Download Generated SDK Package</span>
              </button>
            </div>

          </div>
        )}

      </div>
    </div>
  );
}
