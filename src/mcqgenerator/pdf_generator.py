from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime


def create_result_pdf(mcqs, user_answers, score, percentage, filename="Quiz_Result.pdf"):

    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph("<b>AI MCQ Generator - Quiz Report</b>", styles["Title"]))
    story.append(Paragraph(f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M')}", styles["Normal"]))
    story.append(Paragraph("<br/><br/>", styles["Normal"]))

    story.append(Paragraph(f"<b>Score:</b> {score}/{len(mcqs)}", styles["Heading2"]))
    story.append(Paragraph(f"<b>Percentage:</b> {percentage:.2f}%", styles["Heading2"]))
    story.append(Paragraph("<br/><br/>", styles["Normal"]))

    for i, mcq in enumerate(mcqs):

        story.append(
            Paragraph(
                f"<b>Question {i+1}: {mcq['question']}</b>",
                styles["Heading3"]
            )
        )

        for key, value in mcq["options"].items():
            story.append(
                Paragraph(f"{key}. {value}", styles["Normal"])
            )

        selected = user_answers.get(f"q{i+1}", "Not Answered")

        story.append(
            Paragraph(
                f"<b>Your Answer:</b> {selected}",
                styles["Normal"]
            )
        )

        story.append(
            Paragraph(
                f"<b>Correct Answer:</b> {mcq['correct_answer']}",
                styles["Normal"]
            )
        )

        if selected == mcq["correct_answer"]:
            story.append(
                Paragraph("<font color='green'><b>Correct</b></font>", styles["Normal"])
            )
        else:
            story.append(
                Paragraph("<font color='red'><b>Incorrect</b></font>", styles["Normal"])
            )

        story.append(
            Paragraph(
                f"<b>Explanation:</b> {mcq['explanation']}",
                styles["Normal"]
            )
        )

        story.append(Paragraph("<br/><br/>", styles["Normal"]))

    doc.build(story)

    return filename