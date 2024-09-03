import React, { useRef, useEffect } from 'react';
import * as THREE from 'three';

function AnimatedBackground() {
    const canvasRef = useRef(null);

    useEffect(() => {
        const canvas = canvasRef.current;
        const renderer = new THREE.WebGLRenderer({ canvas, alpha: true });
        renderer.setSize(window.innerWidth, window.innerHeight);

        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        camera.position.z = 30;

        const particlesGeometry = new THREE.BufferGeometry();
        const particlesCount = 5000;

        const posArray = new Float32Array(particlesCount * 3);

        for(let i = 0; i < particlesCount * 3; i++) {
            posArray[i] = (Math.random() - 0.5) * 50;
        }

        particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));

        const particlesMaterial = new THREE.PointsMaterial({
            size: 0.005,
            color: 0x00ffff,
            transparent: true,
            opacity: 0.8,
            blending: THREE.AdditiveBlending
        });

        const particlesMesh = new THREE.Points(particlesGeometry, particlesMaterial);
        scene.add(particlesMesh);

        function animate() {
            requestAnimationFrame(animate);
            particlesMesh.rotation.x += 0.0005;
            particlesMesh.rotation.y += 0.0005;
            renderer.render(scene, camera);
        }
        animate();

        function handleResize() {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        }

        window.addEventListener('resize', handleResize);

        return () => {
            window.removeEventListener('resize', handleResize);
            renderer.dispose();
        };
    }, []);

    return <canvas ref={canvasRef} style={{ position: 'fixed', top: 0, left: 0, zIndex: -1 }} />;
}

export default AnimatedBackground;