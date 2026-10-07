import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ThemeProvider, createTheme, CssBaseline, Box, Typography, Container } from '@mui/material';
import Navbar from './components/Navbar';
import Welcome from './pages/Welcome';
import UploadResume from './pages/UploadResume';
import Results from './pages/Results';
import Interview from './pages/Interview';

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
    primary: {
      main: '#6366f1', // Indigo
      light: '#818cf8',
      dark: '#4f46e5',
    },
    secondary: {
      main: '#a855f7', // Purple
      light: '#c084fc',
      dark: '#9333ea',
    },
    background: {
      default: '#0b0f19',
      paper: '#1e293b',
    },
    text: {
      primary: '#f8fafc',
      secondary: '#94a3b8',
    },
  },
  typography: {
    fontFamily: '"Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
    h4: { fontWeight: 800 },
    h5: { fontWeight: 700 },
    h6: { fontWeight: 700 },
  },
  shape: {
    borderRadius: 12,
  },
});

export default function App() {
  return (
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />
      <Router>
        <Box sx={{ minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
          <Navbar />
          <Box sx={{ flex: 1 }}>
            <Routes>
              <Route path="/" element={<Welcome />} />
              <Route path="/upload" element={<UploadResume />} />
              <Route path="/results" element={<Results />} />
              <Route path="/interview" element={<Interview />} />
            </Routes>
          </Box>
          <Box component="footer" sx={{ py: 3, borderTop: '1px solid rgba(255,255,255,0.06)', textAlign: 'center', backgroundColor: '#070b13' }}>
            <Container maxWidth="xl">
              <Typography variant="body2" sx={{ color: '#64748b' }}>
                CareerLens AI &copy; 2026 — Resume analysis, role matching and job openings in one place.
              </Typography>
            </Container>
          </Box>
        </Box>
      </Router>
    </ThemeProvider>
  );
}
