from sentiment_analysis import score_paragraph
import multitasking

# Define the function to run in parallel
@multitasking.task
def score(chunk_data,index):
    out=score_paragraph(chunk_data)
    print("processing ===>",index)
    return out

if __name__ == "__main__":
    with open("random_parase.txt") as f:
        huge_text = f.read()
        chunks=huge_text.split("\n")
        for i,chunk in enumerate(chunks):
            score(chunk,i)
    multitasking.wait_for_tasks()