function sum(list) {
  if (list.length == 0) {
    return 0;
  } else {
    return list[0] + sum(list.slice(1));
  }
}
console.log(sum([1, 23, 9, 2]));