import pybullet as p
import pybullet_data
import time

# Inicializar simulación
physicsClient = p.connect(p.GUI)  # usar p.DIRECT para modo sin gráficos
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -10)

# Cargar plano y carro
planeId = p.loadURDF("plane.urdf")
carpos = [0, 0, 0.5]
carId = p.loadURDF("cartpole.urdf", carpos, useFixedBase=True)

# Configurar ruedas (simplificado)
wheelIndices = [1, 3]  # Índices de las articulaciones de las ruedas
steeringIndices = [0, 2]  # Articulaciones de dirección

# Simulación
for i in range(1000):
    # Aplicar fuerzas a las ruedas
    p.setJointMotorControl2(
        carId,
        wheelIndices[0],
        p.VELOCITY_CONTROL,
        targetVelocity=5,
        force=10
    )

    p.setJointMotorControl2(
        carId,
        steeringIndices[0],
        p.POSITION_CONTROL,
        targetPosition=0.5,
        force=10
    )

    p.stepSimulation()
    time.sleep(1. / 240)

print("Simulación completada exitosamente")

# Desconectar
p.disconnect()
