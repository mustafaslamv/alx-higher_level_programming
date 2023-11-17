#!/usr/bin/node
exports.esrever = function (list) {
  const len = list.length;
  const result = [];
  for (let i = len - 1; i >= 0; i--) {
    result.push(list[i]);
  }
  return result;
};
