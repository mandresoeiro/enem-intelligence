#!/bin/bash

echo "🛑 Parando ENEM Intelligence..."

# Parar usando PIDs salvos
if [ -f .backend.pid ]; then
    BACKEND_PID=$(cat .backend.pid)
    kill $BACKEND_PID 2>/dev/null && echo "✅ Backend parado (PID: $BACKEND_PID)"
    rm .backend.pid
fi

if [ -f .frontend.pid ]; then
    FRONTEND_PID=$(cat .frontend.pid)
    kill $FRONTEND_PID 2>/dev/null && echo "✅ Frontend parado (PID: $FRONTEND_PID)"
    rm .frontend.pid
fi

# Garantir que tudo foi parado
pkill -f "python manage.py runserver" 2>/dev/null
pkill -f "next dev" 2>/dev/null

echo ""
echo "✅ Projeto parado com sucesso!"
