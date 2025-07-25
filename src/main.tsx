
import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';   // Remove '.tsx' from import (TypeScript handles this automatically)
import './index.css';

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>
);


