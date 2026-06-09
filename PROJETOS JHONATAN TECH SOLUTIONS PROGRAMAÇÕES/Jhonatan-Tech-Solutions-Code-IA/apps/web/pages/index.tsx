import React, { useState, useEffect } from 'react';
import axios from 'axios';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export default function Home() {
  const [apps, setApps] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [formData, setFormData] = useState({
    name: '',
    language: 'python',
    framework: 'fastapi'
  });

  // Carregar apps
  useEffect(() => {
    fetchApps();
  }, []);

  const fetchApps = async () => {
    try {
      setLoading(true);
      const response = await axios.get(`${API_URL}/api/apps`);
      setApps(response.data);
      setError(null);
    } catch (err) {
      setError('Erro ao carregar aplicacoes');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleCreateApp = async (e) => {
    e.preventDefault();
    try {
      await axios.post(`${API_URL}/api/apps`, formData);
      setFormData({ name: '', language: 'python', framework: 'fastapi' });
      fetchApps();
    } catch (err) {
      setError('Erro ao criar aplicacao');
      console.error(err);
    }
  };

  const handleDeleteApp = async (appId) => {
    try {
      await axios.delete(`${API_URL}/api/apps/${appId}`);
      fetchApps();
    } catch (err) {
      setError('Erro ao deletar aplicacao');
      console.error(err);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-600 to-blue-600">
      {/* Header */}
      <header className="bg-white shadow">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <h1 className="text-3xl font-bold text-gray-900">
            🤖 JHONATAN TECH SOLUTIONS CODE AI
          </h1>
          <p className="text-gray-600 mt-2">
            Sistema IA Especializado em Engenharia de Software
          </p>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Error Message */}
        {error && (
          <div className="mb-4 p-4 bg-red-100 border border-red-400 text-red-700 rounded">
            {error}
          </div>
        )}

        {/* Form Section */}
        <div className="bg-white rounded-lg shadow-lg p-8 mb-8">
          <h2 className="text-2xl font-bold mb-6 text-gray-900">
            Criar Nova Aplicacao
          </h2>

          <form onSubmit={handleCreateApp} className="space-y-6">
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              {/* Nome */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Nome da Aplicacao
                </label>
                <input
                  type="text"
                  name="name"
                  value={formData.name}
                  onChange={handleInputChange}
                  required
                  placeholder="Ex: Meu App"
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-600"
                />
              </div>

              {/* Linguagem */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Linguagem
                </label>
                <select
                  name="language"
                  value={formData.language}
                  onChange={handleInputChange}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-600"
                >
                  <option value="python">Python</option>
                  <option value="javascript">JavaScript</option>
                  <option value="typescript">TypeScript</option>
                  <option value="go">Go</option>
                  <option value="java">Java</option>
                  <option value="csharp">C#</option>
                </select>
              </div>

              {/* Framework */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Framework
                </label>
                <select
                  name="framework"
                  value={formData.framework}
                  onChange={handleInputChange}
                  className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-600"
                >
                  <option value="fastapi">FastAPI</option>
                  <option value="react">React</option>
                  <option value="next">Next.js</option>
                  <option value="django">Django</option>
                  <option value="express">Express</option>
                  <option value="gin">Gin</option>
                </select>
              </div>
            </div>

            <button
              type="submit"
              className="w-full bg-purple-600 hover:bg-purple-700 text-white font-bold py-3 px-6 rounded-lg transition"
            >
              Criar Aplicacao
            </button>
          </form>
        </div>

        {/* Apps List */}
        <div className="bg-white rounded-lg shadow-lg p-8">
          <h2 className="text-2xl font-bold mb-6 text-gray-900">
            Minhas Aplicacoes ({apps.length})
          </h2>

          {loading ? (
            <div className="text-center py-8">
              <p className="text-gray-600">Carregando...</p>
            </div>
          ) : apps.length === 0 ? (
            <div className="text-center py-8 bg-gray-50 rounded-lg">
              <p className="text-gray-600">Nenhuma aplicacao criada ainda.</p>
              <p className="text-sm text-gray-500 mt-2">
                Use o formulario acima para criar sua primeira aplicacao!
              </p>
            </div>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {apps.map(app => (
                <div
                  key={app.id}
                  className="border border-gray-200 rounded-lg p-6 hover:shadow-lg transition"
                >
                  <h3 className="text-lg font-bold text-gray-900 mb-2">
                    {app.name}
                  </h3>
                  
                  <div className="space-y-2 mb-4 text-sm">
                    <p>
                      <span className="text-gray-600">Linguagem:</span>
                      <span className="font-semibold ml-2">{app.language}</span>
                    </p>
                    <p>
                      <span className="text-gray-600">Framework:</span>
                      <span className="font-semibold ml-2">{app.framework}</span>
                    </p>
                    <p>
                      <span className="text-gray-600">Status:</span>
                      <span className="font-semibold ml-2 text-green-600">
                        {app.status}
                      </span>
                    </p>
                    <p>
                      <span className="text-gray-600">Criado:</span>
                      <span className="font-semibold ml-2">
                        {new Date(app.created_at).toLocaleDateString()}
                      </span>
                    </p>
                  </div>

                  <button
                    onClick={() => handleDeleteApp(app.id)}
                    className="w-full bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition"
                  >
                    Deletar
                  </button>
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Stats */}
        <div className="mt-8 grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="bg-blue-500 text-white rounded-lg p-6 shadow-lg">
            <h3 className="text-lg font-bold mb-2">Total de Apps</h3>
            <p className="text-4xl font-bold">{apps.length}</p>
          </div>

          <div className="bg-green-500 text-white rounded-lg p-6 shadow-lg">
            <h3 className="text-lg font-bold mb-2">Status</h3>
            <p className="text-2xl font-bold">🟢 Online</p>
          </div>

          <div className="bg-purple-500 text-white rounded-lg p-6 shadow-lg">
            <h3 className="text-lg font-bold mb-2">API</h3>
            <p className="text-sm">Endpoint: /api/apps</p>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-gray-900 text-white mt-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 text-center">
          <p>
            © 2026 JHONATAN TECH SOLUTIONS - CODE AI
          </p>
          <p className="text-sm text-gray-400 mt-2">
            <a href="http://localhost:8000/docs" className="hover:underline">
              📚 API Docs
            </a>
          </p>
        </div>
      </footer>
    </div>
  );
}
