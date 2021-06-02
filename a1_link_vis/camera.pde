void updateCamera() {
  beginCamera();
  camera();
  translate(1024/2, 768/2, -200);
  rotateY(radians(yaw));
  rotateX(radians(pitch));
  endCamera();
}
