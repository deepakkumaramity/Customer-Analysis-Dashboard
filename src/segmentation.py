def segment_customers(df):

    def segment(value):
        if value > 50000:
            return "High Value"
        elif value >= 20000:
            return "Medium Value"
        else:
            return "Low Value"

    df["segment"] = df["revenue"].apply(segment)
    return df
