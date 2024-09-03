import React, { useRef, useEffect, useState } from 'react';
import RubiksCube from './components/RubiksCube';
import AnimatedBackground from './components/AnimatedBackground';
import { motion } from 'framer-motion';

function App() {
    const rotateFace = useRef();
    const [lastRotation, setLastRotation] = useState('');
    const [moveCount, setMoveCount] = useState(0);
    const [timer, setTimer] = useState(0);
    const [isTimerRunning, setIsTimerRunning] = useState(false);
    const [difficulty, setDifficulty] = useState('medium');

    const performRotation = (axis, index, direction) => {
        rotateFace.current(axis, index, direction);
        setLastRotation(`${axis.toUpperCase()}${index} ${direction > 0 ? '↻' : '↺'}`);
        setMoveCount(prev => prev + 1);
        if (!isTimerRunning) {
            setIsTimerRunning(true);
        }
    };

    const resetCube = () => {
        rotateFace.reset();
        setLastRotation('Reset to default');
        setMoveCount(0);
        setTimer(0);
        setIsTimerRunning(false);
    };

    const scrambleCube = () => {
        const moves = difficulty === 'easy' ? 10 : difficulty === 'medium' ? 20 : 30;
        rotateFace.scramble(moves);
        setMoveCount(0);
        setTimer(0);
        setIsTimerRunning(false);
    };

    useEffect(() => {
        let interval;
        if (isTimerRunning) {
            interval = setInterval(() => {
                setTimer(prev => prev + 1);
            }, 1000);
        }
        return () => clearInterval(interval);
    }, [isTimerRunning]);

    useEffect(() => {
        const handleKeyDown = (event) => {
            const keyMappings = {
                'ArrowUp': () => performRotation('y', 1, 1),
                'ArrowDown': () => performRotation('y', 1, -1),
                'ArrowLeft': () => performRotation('x', 1, -1),
                'ArrowRight': () => performRotation('x', 1, 1),
                'w': () => performRotation('x', -1, 1),
                's': () => performRotation('x', -1, -1),
                'a': () => performRotation('y', -1, -1),
                'd': () => performRotation('y', -1, 1),
                'q': () => performRotation('z', 1, 1),
                'e': () => performRotation('z', 1, -1),
            };

            if (keyMappings[event.key]) {
                keyMappings[event.key]();
            }
        };

        window.addEventListener('keydown', handleKeyDown);
        return () => window.removeEventListener('keydown', handleKeyDown);
    }, []);

    return (
        <div style={{ 
            width: '100vw', 
            height: '100vh', 
            display: 'flex', 
            flexDirection: 'column',
            overflow: 'hidden',
            position: 'relative',
            background: '#1a1a1a',
            fontFamily: 'Arial, sans-serif',
        }}>
            <AnimatedBackground />
            <div style={{ flex: 1, position: 'relative', zIndex: 1 }}>
                <RubiksCube rotateFace={rotateFace} onMoveComplete={() => setMoveCount(prev => prev + 1)} />
                <motion.div 
                    initial={{ opacity: 0, y: -50 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.5 }}
                    style={{ 
                        position: 'absolute', 
                        top: 10, 
                        left: 10, 
                        color: 'white', 
                        background: 'rgba(0,0,0,0.7)', 
                        padding: '10px',
                        borderRadius: '5px',
                        display: 'flex',
                        flexDirection: 'column',
                        gap: '5px',
                    }}
                >
                    <div>Last action: {lastRotation}</div>
                    <div>Moves: {moveCount}</div>
                    <div>Time: {Math.floor(timer / 60)}:{(timer % 60).toString().padStart(2, '0')}</div>
                    <div>
                        Difficulty: 
                        <select value={difficulty} onChange={(e) => setDifficulty(e.target.value)} style={selectStyle}>
                            <option value="easy">Easy</option>
                            <option value="medium">Medium</option>
                            <option value="hard">Hard</option>
                        </select>
                    </div>
                </motion.div>
            </div>
            <motion.div 
                initial={{ opacity: 0, y: 50 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5 }}
                style={{ 
                    padding: '20px', 
                    display: 'flex', 
                    justifyContent: 'center', 
                    background: 'rgba(0, 0, 0, 0.8)',
                    boxShadow: '0px -5px 10px rgba(0, 0, 0, 0.2)'
                }}
            >
                {['x', 'y', 'z'].map(axis => (
                    <div key={axis} style={{ margin: '0 10px' }}>
                        <motion.button 
                            whileHover={{ scale: 1.1 }}
                            whileTap={{ scale: 0.9 }}
                            onClick={() => performRotation(axis, 1, 1)} 
                            style={buttonStyle}
                        >
                            Rotate {axis.toUpperCase()}1 ↻
                        </motion.button>
                        <motion.button 
                            whileHover={{ scale: 1.1 }}
                            whileTap={{ scale: 0.9 }}
                            onClick={() => performRotation(axis, 1, -1)} 
                            style={buttonStyle}
                        >
                            Rotate {axis.toUpperCase()}1 ↺
                        </motion.button>
                    </div>
                ))}
                <div style={{ margin: '0 10px' }}>
                    <motion.button 
                        whileHover={{ scale: 1.1 }}
                        whileTap={{ scale: 0.9 }}
                        onClick={resetCube} 
                        style={{...buttonStyle, background: '#ff3b30'}}
                    >
                        Reset Cube
                    </motion.button>
                    <motion.button 
                        whileHover={{ scale: 1.1 }}
                        whileTap={{ scale: 0.9 }}
                        onClick={scrambleCube} 
                        style={{...buttonStyle, background: '#5856d6'}}
                    >
                        Scramble
                    </motion.button>
                </div>
            </motion.div>
        </div>
    );
}

const buttonStyle = {
    padding: '10px 15px',
    margin: '5px',
    fontSize: '14px',
    background: '#007aff',
    color: 'white',
    border: 'none',
    borderRadius: '5px',
    cursor: 'pointer',
    transition: 'background 0.3s',
};

const selectStyle = {
    marginLeft: '5px',
    padding: '2px 5px',
    background: '#007aff',
    color: 'white',
    border: 'none',
    borderRadius: '3px',
    cursor: 'pointer',
};

export default App;