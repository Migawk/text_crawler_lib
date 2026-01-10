# Description
Searching words by sense of the phrase.

## Why is it cool
Lots of search engines provides a searching by keywords.

**So... Why it's better that the usual engines?**
1. Search by text is TOO SLOW because it requires to compare strings. Actually for programmers [recommended to avoid this approach](https://romgrk.com/posts/optimizing-javascript#1-avoid-string-comparisons).
2. You can find more, spending less time and resources. Analyze > Search
3. Actually here I'd explain about synonyms, anthonyms, double-meaning of the words, etc.
If you understand why it's useful for you, pick one and test.

*⚠️ ( might be used for comparing phrases, I didn't mean to use only for searching )*

## Usage
For the first prepare vectors voccabular. I took one from [Glove](https://nlp.stanford.edu/projects/glove/)
Everything in `core.py`.

`vectorize_phrase` - search through words, vectorize, normalize and finds the average value of them that might be used for comparisation.
`euclidean_distance` - counts the distance of those vectors. As close to 0 as better.
`cosine_similarity` - counts the degree between vectors. As close to 1 as better.

I recommend to use `euclidean_distance`, due to it much more useful for phrases, not words.

### Example
```py
phrase1 = vectorize_phrase("sister is cooking")
phrase2 = vectorize_phrase("sister on the kitchen")

vectors_distance = euclidean_distance(phrase1, phrase2)

print(vectors_distance) # 0.3553 - pretty close to each other phrases
```
