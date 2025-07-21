import subprocess
import sys

def check_and_install_dependencies():
    """
    Checks for and installs required Python packages for SadTalker.
    """

    required_packages = [
        "torch",
        "torchvision",
        "torchaudio",
        "opencv-python",
        "opencv-contrib-python",
        "pydub",
        "numpy",
        "matplotlib",
        "scipy",
        "imageio",
        "tqdm",
        "gfpgan",
        "face_alignment",
    ]

    def is_package_installed(package_name):
        """Check if a package is installed."""
        try:
            __import__(package_name)
            return True
        except ImportError:
            return False

    print("\n🔍 Checking and installing SadTalker dependencies...\n")

    for pkg in required_packages:
        base_pkg = pkg.split('==')[0]  # to handle versioned packages
        if not is_package_installed(base_pkg):
            print(f"📦 Installing missing package: {pkg} ...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
        else:
            print(f"✅ {pkg} is already installed.")

    print("\n✅ All SadTalker dependencies are checked and installed.\n")
check_and_install_dependencies()