import React, { useRef, useState, useEffect } from 'react';
import { Canvas, useFrame, extend } from '@react-three/fiber';
import { OrbitControls } from '@react-three/drei';
import * as THREE from 'three';

const cubeSize = 0.95;
const spacing = 0.1;
const colors = [0xff3b30, 0x4cd964, 0x007aff, 0xffcc00, 0xff9500, 0xffffff].map(c => new THREE.Color(c));

function Cube({ position, materials, rotation }) {
    const ref = useRef();

    useFrame(() => {
        if (ref.current) {
            ref.current.rotation.x = THREE.MathUtils.lerp(ref.current.rotation.x, rotation[0], 0.1);
            ref.current.rotation.y = THREE.MathUtils.lerp(ref.current.rotation.y, rotation[1], 0.1);
            ref.current.rotation.z = THREE.MathUtils.lerp(ref.current.rotation.z, rotation[2], 0.1);
        }
    });

    return (
        <mesh ref={ref} position={position} castShadow receiveShadow>
            <boxGeometry args={[cubeSize, cubeSize, cubeSize]} />
            {materials.map((material, index) => (
                <meshStandardMaterial 
                    key={index} 
                    attach={`material-${index}`} 
                    color={material.color}
                    roughness={0.1}
                    metalness={0.5}
                    emissive={material.color}
                    emissiveIntensity={0.2}
                />
            ))}
        </mesh>
    );
}

function RubiksCube({ rotateFace, onMoveComplete }) {
    const [cubes, setCubes] = useState(() => {
        const initialCubes = [];
        for (let x = -1; x <= 1; x++) {
            for (let y = -1; y <= 1; y++) {
                for (let z = -1; z <= 1; z++) {
                    const materials = colors.map(color => new THREE.MeshStandardMaterial({ color }));
                    initialCubes.push({
                        position: [x * (cubeSize + spacing), y * (cubeSize + spacing), z * (cubeSize + spacing)],
                        materials,
                        rotation: [0, 0, 0],
                    });
                }
            }
        }
        return initialCubes;
    });

    const rotateMatrix = (matrix, axis) => {
        const rotated = [...matrix];
        if (axis === 'x') {
            [rotated[1], rotated[2], rotated[4], rotated[5]] = [rotated[4], rotated[5], rotated[2], rotated[1]];
        } else if (axis === 'y') {
            [rotated[0], rotated[2], rotated[3], rotated[5]] = [rotated[3], rotated[0], rotated[5], rotated[2]];
        } else if (axis === 'z') {
            [rotated[0], rotated[1], rotated[3], rotated[4]] = [rotated[1], rotated[4], rotated[0], rotated[3]];
        }
        return rotated;
    };

    const resetCube = () => {
        setCubes(() => {
            const initialCubes = [];
            for (let x = -1; x <= 1; x++) {
                for (let y = -1; y <= 1; y++) {
                    for (let z = -1; z <= 1; z++) {
                        const materials = colors.map(color => new THREE.MeshStandardMaterial({ color }));
                        initialCubes.push({
                            position: [x * (cubeSize + spacing), y * (cubeSize + spacing), z * (cubeSize + spacing)],
                            materials,
                            rotation: [0, 0, 0],
                        });
                    }
                }
            }
            return initialCubes;
        });
    };

    const scrambleCube = (moves = 20) => {
        const axes = ['x', 'y', 'z'];
        const directions = [1, -1];
        for (let i = 0; i < moves; i++) {
            const axis = axes[Math.floor(Math.random() * 3)];
            const index = Math.floor(Math.random() * 3) - 1;
            const direction = directions[Math.floor(Math.random() * 2)];
            rotateFace.current(axis, index, direction);
        }
    };

    useEffect(() => {
        rotateFace.current = (axis, index, direction) => {
            setCubes(prevCubes => {
                const newCubes = [...prevCubes];
                const faceIndices = newCubes.reduce((acc, cube, i) => {
                    const axisIndex = axis === 'x' ? 0 : axis === 'y' ? 1 : 2;
                    if (Math.round(cube.position[axisIndex]) === index) {
                        acc.push(i);
                    }
                    return acc;
                }, []);

                const rotationAngle = direction * Math.PI / 2;
                const rotationAxis = new THREE.Vector3(axis === 'x' ? 1 : 0, axis === 'y' ? 1 : 0, axis === 'z' ? 1 : 0);
                const rotationMatrix = new THREE.Matrix4().makeRotationAxis(rotationAxis, rotationAngle);

                faceIndices.forEach(i => {
                    const cube = newCubes[i];
                    const position = new THREE.Vector3(...cube.position);
                    position.applyMatrix4(rotationMatrix);
                    cube.position = position.toArray();

                    const currentRotation = new THREE.Euler(...cube.rotation);
                    const quaternion = new THREE.Quaternion().setFromEuler(currentRotation);
                    const rotationQuaternion = new THREE.Quaternion().setFromAxisAngle(rotationAxis, rotationAngle);
                    quaternion.multiply(rotationQuaternion);
                    const newRotation = new THREE.Euler().setFromQuaternion(quaternion);
                    cube.rotation = [newRotation.x, newRotation.y, newRotation.z];

                    cube.materials = rotateMatrix(cube.materials, axis);
                });

                return newCubes;
            });
        };
        rotateFace.reset = resetCube;
        rotateFace.scramble = scrambleCube;
    }, [onMoveComplete]);

    return (
        <Canvas shadows camera={{ position: [5, 5, 5], fov: 50 }}>
            <color attach="background" args={['#000000']} />
            <ambientLight intensity={0.4} />
            <pointLight position={[10, 10, 10]} intensity={1} castShadow />
            <pointLight position={[-10, -10, -10]} intensity={0.5} />
            <group rotation={[Math.PI / 6, -Math.PI / 4, 0]}>
                {cubes.map((cube, i) => (
                    <Cube key={i} position={cube.position} materials={cube.materials} rotation={cube.rotation} />
                ))}
            </group>
            <OrbitControls enablePan={false} enableZoom={true} minPolarAngle={Math.PI / 4} maxPolarAngle={Math.PI - Math.PI / 4} />
        </Canvas>
    );
}

export default RubiksCube;