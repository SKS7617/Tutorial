{ pkgs }: {
  deps = [
    pkgs.python3
    pkgs.python3Packages.pip
    pkgs.python3Packages.numpy  # Add numpy
    pkgs.opencv                 # Add OpenCV
  ];
}