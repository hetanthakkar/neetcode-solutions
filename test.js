function solution(S) {
  let counter = 0;
  let V = parseInt(S, 2);
  console.log(V);
  while (V > 0) {
    console.log(V, counter);
    if ((V & 1) === 0) {
      V = V >>= 1;
    } else {
      V = V - 1;
    }
    counter++;
  }
  return counter;
}

console.log(solution([1]));
