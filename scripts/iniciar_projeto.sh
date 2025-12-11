#!/bin/bash

echo "🚀 Iniciando ENEM Intelligence..."

# Cores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Matar processos anteriores
echo "🧹 Limpando processos antigos..."
pkill -f "python manage.py runserver" 2>/dev/null
pkill -f "next dev" 2>/dev/null
sleep 2

# Iniciar Backend
echo -e "${BLUE}📦 Iniciando Backend Django...${NC}"
cd backend
source .venv/bin/activate 2>/dev/null || python -m venv .venv && source .venv/bin/activate
python manage.py runserver 8000 > ../backend.log 2>&1 &
BACKEND_PID=$!
echo -e "${GREEN}✅ Backend rodando na porta 8000 (PID: $BACKEND_PID)${NC}"
cd ..

# Aguardar backend iniciar
sleep 3

# Iniciar Frontend
echo -e "${BLUE}🎨 Iniciando Frontend Next.js...${NC}"
cd frontend
npm run dev > ../frontend.log 2>&1 &
FRONTEND_PID=$!
echo -e "${GREEN}✅ Frontend rodando na porta 3000 (PID: $FRONTEND_PID)${NC}"
cd ..

# Salvar PIDs para parar depois
echo $BACKEND_PID > .backend.pid
echo $FRONTEND_PID > .frontend.pid

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "${GREEN}✅ Projeto iniciado com sucesso!${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📍 URLs:"
echo "   Frontend: http://localhost:3000"
echo "   Backend:  http://localhost:8000"
echo "   Admin:    http://localhost:8000/admin"
echo ""
echo "📋 Comandos úteis:"
echo "   Ver logs backend:  tail -f backend.log"
echo "   Ver logs frontend: tail -f frontend.log"
echo "   Parar tudo:        ./parar_projeto.sh"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
