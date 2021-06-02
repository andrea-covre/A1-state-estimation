void skeletonTracing(int backFrames) {
  for (int i = 1; i <= backFrames; i++) {
    if(drawTracing && time-i >= 0) {
      updateDataPoint(time-i);
      drawSkeleton(180/backFrames * (backFrames-i));
    }
  }
}
