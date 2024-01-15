from tokenizers import BertWordPieceTokenizer
bert_wordpiece_tokenizer = BertWordPieceTokenizer()
bert_wordpiece_tokenizer.train("corpus.txt")
#print(bert_wordpiece_tokenizer.get_vocab())
bert_wordpiece_tokenizer.save_model("tokenizer")