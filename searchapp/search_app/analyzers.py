from elasticsearch_dsl import analysis, analyzer, tokenizer


class CustomAnalyzer:
    @property
    def ngram_1(self):
        ngram_filter = analysis.token_filter(
            "ngram_3", "ngram", min_gram=4, max_gram=4)
        return analyzer("text_analyzer",
                        tokenizer="whitespace",
                        filter=["lowercase", ngram_filter])
    
    def autocomplete(self):
        autocomplete_filter = analysis.token_filter(
            "autocomplete_filter",
            "edge_ngram",
            min_gram=1,
            max_gram=20
        )
        return analyzer(
            "autocomplete",
            type="custom",
            tokenizer="standard",
            filter=["lowercase", autocomplete_filter]
        )
