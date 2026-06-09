import React, { useState, useEffect } from 'react';
import { View, Text, TouchableOpacity, ScrollView, ActivityIndicator, Alert } from 'react-native';
import axios from 'axios';

const API_URL = 'http://localhost:8000';

export default function App() {
  const [apps, setApps] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchApps();
  }, []);

  const fetchApps = async () => {
    try {
      setLoading(true);
      const response = await axios.get(`${API_URL}/api/apps`);
      setApps(response.data);
    } catch (error) {
      Alert.alert('Erro', 'Nao foi possivel carregar as aplicacoes');
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  const handleCreateApp = async () => {
    try {
      await axios.post(`${API_URL}/api/apps`, {
        name: 'Novo App',
        language: 'python',
        framework: 'fastapi'
      });
      fetchApps();
      Alert.alert('Sucesso', 'Aplicacao criada!');
    } catch (error) {
      Alert.alert('Erro', 'Falha ao criar aplicacao');
    }
  };

  const handleDeleteApp = async (appId) => {
    try {
      await axios.delete(`${API_URL}/api/apps/${appId}`);
      fetchApps();
      Alert.alert('Sucesso', 'Aplicacao deletada!');
    } catch (error) {
      Alert.alert('Erro', 'Falha ao deletar');
    }
  };

  return (
    <View style={{ flex: 1, backgroundColor: '#f5f5f5' }}>
      {/* Header */}
      <View style={{
        backgroundColor: '#667eea',
        paddingTop: 40,
        paddingBottom: 20,
        paddingHorizontal: 16
      }}>
        <Text style={{
          fontSize: 24,
          fontWeight: 'bold',
          color: 'white',
          marginBottom: 8
        }}>
          🤖 JHONATAN CODE AI
        </Text>
        <Text style={{ color: 'rgba(255,255,255,0.8)', fontSize: 14 }}>
          Engenharia de Software com IA
        </Text>
      </View>

      {/* Content */}
      <ScrollView style={{ flex: 1, padding: 16 }}>
        {/* Create Button */}
        <TouchableOpacity
          onPress={handleCreateApp}
          style={{
            backgroundColor: '#667eea',
            paddingVertical: 12,
            paddingHorizontal: 16,
            borderRadius: 8,
            marginBottom: 20
          }}
        >
          <Text style={{ color: 'white', fontWeight: 'bold', textAlign: 'center' }}>
            + Criar Aplicacao
          </Text>
        </TouchableOpacity>

        {/* Loading */}
        {loading ? (
          <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center', marginTop: 40 }}>
            <ActivityIndicator size="large" color="#667eea" />
          </View>
        ) : apps.length === 0 ? (
          <View style={{
            backgroundColor: 'white',
            padding: 20,
            borderRadius: 8,
            marginTop: 20,
            alignItems: 'center'
          }}>
            <Text style={{ fontSize: 16, color: '#666', marginBottom: 8 }}>
              Nenhuma aplicacao criada
            </Text>
            <Text style={{ fontSize: 12, color: '#999' }}>
              Use o botao acima para criar sua primeira aplicacao!
            </Text>
          </View>
        ) : (
          apps.map(app => (
            <View
              key={app.id}
              style={{
                backgroundColor: 'white',
                padding: 16,
                borderRadius: 8,
                marginBottom: 12,
                borderLeftWidth: 4,
                borderLeftColor: '#667eea'
              }}
            >
              <Text style={{ fontSize: 16, fontWeight: 'bold', marginBottom: 8 }}>
                {app.name}
              </Text>
              
              <Text style={{ fontSize: 12, color: '#666', marginBottom: 4 }}>
                Linguagem: {app.language}
              </Text>
              <Text style={{ fontSize: 12, color: '#666', marginBottom: 12 }}>
                Framework: {app.framework}
              </Text>

              <TouchableOpacity
                onPress={() => handleDeleteApp(app.id)}
                style={{
                  backgroundColor: '#ff6b6b',
                  paddingVertical: 8,
                  paddingHorizontal: 12,
                  borderRadius: 4
                }}
              >
                <Text style={{ color: 'white', fontWeight: 'bold', textAlign: 'center', fontSize: 12 }}>
                  Deletar
                </Text>
              </TouchableOpacity>
            </View>
          ))
        )}
      </ScrollView>

      {/* Footer */}
      <View style={{
        backgroundColor: '#333',
        paddingVertical: 12,
        paddingHorizontal: 16,
        alignItems: 'center'
      }}>
        <Text style={{ color: 'white', fontSize: 12 }}>
          © 2026 JHONATAN TECH SOLUTIONS
        </Text>
      </View>
    </View>
  );
}
