To create a naming scheme generator function, we can use the following code:

```javascript
const adjectives = {
  a: ['angry', 'anxious', 'amused', 'adorable', 'amazing', 'ambitious', 'artistic'],
  b: ['brave', 'bored', 'bitter', 'bold', 'bashful', 'bewildered', 'benevolent'],
  // ...
  z: ['zealous', 'zany', 'zestful', 'zen', 'zippy', 'zombie-like', 'zigzag']
};

const nouns = {
  a: ['abyss', 'angel', 'artifact', 'anomaly', 'algorithm', 'atmosphere', 'antenna'],
  b: ['beacon', 'bubble', 'boundary', 'balance', 'butterfly', 'breeze', 'blossom'],
  // ...
  z: ['zenith', 'zephyr', 'zone', 'zodiac', 'zigzag', 'zombie', 'zeppelin']
};

function getRandomElement(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

function generateRandomName() {
  const randomLetter = String.fromCharCode(97 + Math.floor(Math.random() * 26));
  const adjective = getRandomElement(adjectives[randomLetter]);
  const noun = getRandomElement(nouns[randomLetter]);
  return `${adjective}-${noun}`;
}

console.log(generateRandomName());
```

This code defines two objects, `adjectives` and `nouns`, each containing arrays of words for every letter of the alphabet. The `getRandomElement` function returns a random element from an array, and the `generateRandomName` function generates a random name by selecting a random letter, then choosing a random adjective and noun from the corresponding arrays. Finally, the generated name is printed to the console.