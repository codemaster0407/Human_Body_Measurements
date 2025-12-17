# Human Body Measurements

An automated 3D body measurement system that extracts precise body measurements (chest, waist, shoulder, wrist, elbow) from 3D human body models using Blender's Python API (bpy) and provides 2D-to-3D coordinate mapping capabilities.

## 📋 Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Prerequisites \& Dependencies](#prerequisites--dependencies)
- [Blender Python API (bpy) Setup](#blender-python-api-bpy-setup)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Measurement Modules](#measurement-modules)
- [2D-3D Mapping](#2d-3d-mapping)
- [Examples](#examples)
- [License](#license)

## 🎯 Overview

This project is an undergraduate research initiative focused on automating human body measurements from 3D models. The system leverages **Blender's Python API (bpy)** to manipulate 3D meshes, extract key anatomical points, and calculate circumference measurements at various body locations. Additionally, it includes 2D pose detection using MediaPipe and neural network-based prediction models.

### Primary Applications:
- Automated garment sizing from 3D body scans
- Virtual fitting and e-commerce
- Anthropometric data collection
- Custom tailoring measurements

## ✨ Key Features

- **3D Mesh Analysis**: Load and analyze OBJ files containing human body models
- **Automated Measurements**: Calculate chest, waist, shoulder, wrist, and elbow circumferences
- **Blender Integration**: Utilizes Blender's powerful mesh manipulation tools via Python scripting
- **2D Pose Detection**: Extract body landmarks from 2D images using MediaPipe
- **2D-3D Mapping**: Transform 2D coordinates to 3D space
- **Neural Network Predictions**: Machine learning models for measurement estimation
- **Batch Processing**: Process multiple models simultaneously

## 📦 Prerequisites & Dependencies

### Core Dependencies
- **Python**: 3.7 or higher
- **Blender**: 2.93+ (required for bpy)
- **NumPy**: Array operations and mathematical computations
- **OpenCV (cv2)**: Image processing
- **MediaPipe**: 2D pose landmark detection
- **Pandas**: Data handling and CSV operations
- **Matplotlib**: Visualization (optional)

### Python Libraries
Install the following libraries using pip:
```bash
pip install numpy opencv-python mediapipe pandas matplotlib
```

## 🔧 Blender Python API (bpy) Setup

> [!IMPORTANT]
> **Blender Python (bpy)** is the core dependency for this project. It provides programmatic access to Blender's 3D modeling and mesh analysis capabilities. This section is crucial for setting up your environment.

### What is bpy?

`bpy` is Blender's Python API that allows you to:
- Load and manipulate 3D models (OBJ, STL, FBX, etc.)
- Access mesh data (vertices, edges, faces)
- Perform geometric operations and measurements
- Automate Blender operations via scripting

### Installation Methods

You have **two main options** for using bpy with this project:

#### **Option 1: Run Scripts Inside Blender (Recommended for Beginners)**

1. **Download Blender**:
   - Visit [https://www.blender.org/download/](https://www.blender.org/download/)
   - Download Blender 2.93 or later
   - Install following the platform-specific instructions

2. **Run Python Scripts in Blender**:
   - Open Blender
   - Switch to the "Scripting" workspace (top menu bar)
   - Open your Python script in the text editor
   - Click "Run Script" or press `Alt + P`
   - View output in the system console

3. **Access System Console** (to see print statements):
   - **Windows**: `Window` → `Toggle System Console`
   - **macOS/Linux**: Run Blender from terminal: `/Applications/Blender.app/Contents/MacOS/Blender`

#### **Option 2: Install bpy as a Python Module (Advanced)**

Install bpy as a standalone Python module using pip:

```bash
pip install bpy
```

> [!WARNING]
> **Known Issues with pip installation**:
> - The `bpy` PyPI package may not include all Blender features
> - Version compatibility can be problematic
> - Platform-specific build issues are common
> - Some Blender operations require the full application

**Alternative for standalone bpy**:
Use the official Blender Python module build:

```bash
# For macOS/Linux - Use Blender's Python interpreter
/Applications/Blender.app/Contents/Resources/2.93/python/bin/python3.9 -m pip install <package>

# For Windows
"C:\Program Files\Blender Foundation\Blender 2.93\2.93\python\bin\python.exe" -m pip install <package>
```

Then use Blender's Python to run your scripts:
```bash
blender --background --python your_script.py
```

### Verifying bpy Installation

Test your bpy installation with this simple script:

```python
import bpy

# Print Blender version
print(f"Blender version: {bpy.app.version_string}")

# Create a simple cube
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
print("Cube created successfully!")

# Access mesh data
obj = bpy.context.active_object
print(f"Number of vertices: {len(obj.data.vertices)}")
```

**Expected output**:
```
Blender version: 2.93.x
Cube created successfully!
Number of vertices: 8
```

### Using bpy in This Project

All measurement scripts in the `final_functions/` directory use bpy to:

1. **Import 3D models**:
   ```python
   bpy.ops.import_scene.obj(filepath=path)
   ```

2. **Access mesh vertices**:
   ```python
   mesh = bpy.data.objects[object_name].data
   vertices = [v.co for v in mesh.vertices]
   ```

3. **Perform mesh operations**:
   ```python
   bpy.ops.mesh.bisect(plane_co=(x, y, z), plane_no=(0, 0, 1))
   ```

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Human_Body_Measurements.git
   cd Human_Body_Measurements
   ```

2. **Install Python dependencies**:
   ```bash
   pip install numpy opencv-python mediapipe pandas matplotlib
   ```

3. **Set up Blender** (see [Blender Python API Setup](#blender-python-api-bpy-setup) above)

4. **Prepare your 3D models**:
   - Place OBJ files in the `obj_files/` directory
   - Ensure models are human body scans in a standard T-pose or A-pose

## 📁 Project Structure

```
Human_Body_Measurements/
├── final_functions/          # Production-ready measurement modules
│   ├── driver.py            # Main orchestration script
│   ├── final_chest.py       # Chest circumference calculation
│   ├── final_waist.py       # Waist circumference calculation
│   ├── final_shoulder.py    # Shoulder width measurement
│   ├── final_lefthand.py    # Left arm measurements
│   ├── final_righthand.py   # Right arm measurements
│   ├── wrist.py             # Wrist circumference
│   └── anchor_points.py     # Reference point detection
│
├── 2D-3Dmapping/            # 2D to 3D coordinate transformation
│   ├── 2Dpoints.py          # MediaPipe pose landmark extraction
│   ├── bg_removal.py        # Background removal preprocessing
│   ├── transformation.py    # Coordinate transformation logic
│   └── 2d_3dmapping.ipynb   # Jupyter notebook for mapping
│
├── neural_networks/         # Machine learning models
│   ├── training_model.pkl   # Trained regression model
│   └── model_load.ipynb     # Model loading examples
│
├── obj_files/               # 3D model storage (OBJ format)
├── Photos/                  # 2D image dataset
├── functions/               # Legacy/experimental functions
├── final_code/              # Alternative implementations
├── experimentation/         # Testing and prototyping
├── annotations.csv          # Manual measurement annotations
├── blender_measurements.csv # Extracted measurements
└── README.md                # This file
```

## 💻 Usage

### Running Measurements with Blender

#### Method 1: Using the Driver Script

The `driver.py` script runs all measurement functions sequentially:

```python
# Edit driver.py to set your OBJ file path
path = "/path/to/your/model.obj"
object_name = "model_name"

# Run all measurements
final_chest.chest_function(path, object_name)
wrist.wrist_function(path, object_name)
final_waist.waist_function(path, object_name)
final_righthand.right_hand_function(path, object_name)
final_lefthand.left_hand_function(path, object_name)
final_shoulder.shoulder_function(path, object_name)
```

**Execute in Blender**:
```bash
blender --background --python final_functions/driver.py
```

#### Method 2: Individual Measurement Modules

Run specific measurement scripts:

```python
import bpy
from final_functions import final_chest

# Path to your 3D model
model_path = "obj_files/your_model.obj"
model_name = "your_model"

# Calculate chest circumference
final_chest.chest_function(model_path, model_name)
```

### 2D Pose Detection

Extract body landmarks from images:

```python
from 2D-3Dmapping import 2Dpoints

# Process an image
image_path = "Photos/person.jpg"
coordinates = 2Dpoints.normalized_coordinates(image_path)
print(f"Detected landmarks: {len(coordinates)}")
```

## 📐 Measurement Modules

### Chest Circumference (`final_chest.py`)
- Locates chest plane at 30% body height from top
- Bisects mesh at chest line
- Counts vertices and calculates circumference

### Waist Circumference (`final_waist.py`)
- Identifies waist plane at 47% body height from top
- Measures horizontal circumference

### Shoulder Width (`final_shoulder.py`)
- Detects shoulder line at 22-24.6% from top
- Calculates width between shoulder points

### Wrist Circumference (`wrist.py`)
- Locates wrist position on each arm
- Computes circumference at wrist plane

### Elbow Measurements
- `final_lefthand.py` - Left elbow circumference
- `final_righthand.py` - Right elbow circumference

### Measurement Algorithm

All modules follow this general pattern:

1. **Import Model**: Load OBJ file using `bpy.ops.import_scene.obj()`
2. **Find Extremes**: Locate highest and lowest points on the model
3. **Calculate Reference Heights**: Compute anatomical landmarks as percentages of total height
4. **Mesh Bisection**: Use `bpy.ops.mesh.bisect()` to slice mesh at measurement plane
5. **Vertex Counting**: Count vertices at the cross-section
6. **Circumference Calculation**: Multiply vertex count by edge length

## 🔄 2D-3D Mapping

The project includes tools to map 2D image coordinates to 3D model space:

### MediaPipe Integration
- Uses MediaPipe Pose to detect 33 body landmarks
- Normalizes coordinates based on image dimensions
- Supports background removal for better detection

### Workflow
1. **Capture Image**: Take 2D photo of subject
2. **Remove Background**: Optional preprocessing (`bg_removal.py`)
3. **Detect Landmarks**: Extract pose keypoints (`2Dpoints.py`)
4. **Transform to 3D**: Map 2D coordinates to 3D space (`transformation.py`)

## 📊 Examples

### Example Output

Running the chest measurement script:

```bash
$ blender --background --python final_functions/final_chest.py

Chest circumference is 98.47 cm
Error between original and predicted: -3.47 cm
```

### Sample Model Processing

```python
# Process multiple models
models = [
    "obj_files/person_1.obj",
    "obj_files/person_2.obj",
    "obj_files/person_3.obj"
]

for model_path in models:
    model_name = model_path.split('/')[-1].split('.')[0]
    print(f"\nProcessing: {model_name}")
    
    chest_circ = final_chest.chest_function(model_path, model_name)
    waist_circ = final_waist.waist_function(model_path, model_name)
    shoulder_width = final_shoulder.shoulder_function(model_path, model_name)
```

## 🤝 Contributing

This is an undergraduate research project. Contributions, suggestions, and improvements are welcome!

### Areas for Improvement
- Enhanced accuracy in measurement algorithms
- Support for more body measurements (hips, thigh, neck)
- Real-time measurement from depth cameras
- GUI application for easier usage
- Better 2D-3D mapping accuracy

## 📄 License

This project is licensed under the **Eclipse Public License v2.0** - see the [LICENSE](LICENSE) file for details.

## 📚 References

- [Blender Python API Documentation](https://docs.blender.org/api/current/)
- [MediaPipe Pose Documentation](https://google.github.io/mediapipe/solutions/pose)
- [NumPy Documentation](https://numpy.org/doc/)

## 👥 Authors

Undergraduate Project Team  
Course Project on Human Body Measurements

---

## 🐛 Troubleshooting

### Common Issues

**"No module named 'bpy'"**
- Ensure you're running scripts inside Blender or using Blender's Python interpreter
- See [Blender Python API Setup](#blender-python-api-bpy-setup)

**"AttributeError: 'NoneType' object has no attribute 'data'"**
- Check that your OBJ file path is correct
- Verify the object name matches the imported model name

**Measurements seem inaccurate**
- Ensure your model is in standard pose (T-pose or A-pose)
- Verify the model scale is in centimeters or adjust the edge length calibration

**MediaPipe not detecting pose**
- Check image quality and lighting
- Ensure full body is visible in the frame
- Try background removal preprocessing

---

**Need Help?** Open an issue in the repository with your error message and system details.
