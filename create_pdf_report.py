from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image, Table, TableStyle,
    KeepTogether
)

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "EV_Charging_Project_Report.pdf"
FIG = ROOT / "figures"

NAVY = colors.HexColor("#153B5B")
BLUE = colors.HexColor("#2E86AB")
LIGHT = colors.HexColor("#EAF3F7")
ORANGE = colors.HexColor("#F18F01")
GRAY = colors.HexColor("#5B6573")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="ReportTitle", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=23, leading=28, textColor=NAVY, alignment=TA_CENTER, spaceAfter=16))
styles.add(ParagraphStyle(name="Subtitle", parent=styles["Normal"], fontSize=12, leading=17, textColor=GRAY, alignment=TA_CENTER, spaceAfter=14))
styles.add(ParagraphStyle(name="H1x", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=16, leading=20, textColor=NAVY, spaceBefore=8, spaceAfter=10))
styles.add(ParagraphStyle(name="H2x", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=12.5, leading=16, textColor=BLUE, spaceBefore=8, spaceAfter=6))
styles.add(ParagraphStyle(name="Bodyx", parent=styles["BodyText"], fontSize=9.6, leading=14, textColor=colors.HexColor("#263238"), spaceAfter=7))
styles.add(ParagraphStyle(name="Smallx", parent=styles["BodyText"], fontSize=8.2, leading=11, textColor=GRAY, spaceAfter=4))
styles.add(ParagraphStyle(name="Callout", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=10.5, leading=15, textColor=NAVY, backColor=LIGHT, borderColor=BLUE, borderWidth=0.6, borderPadding=10, spaceBefore=5, spaceAfter=10))

def p(text, style="Bodyx"):
    return Paragraph(text, styles[style])

def bullet(text):
    return Paragraph("• " + text, ParagraphStyle(name="bullet_temp", parent=styles["Bodyx"], leftIndent=13, firstLineIndent=-8, spaceAfter=5))

def figure(path, caption, width=7.0*inch):
    img = Image(str(FIG/path))
    ratio = img.imageHeight / img.imageWidth
    img.drawWidth = width
    img.drawHeight = width * ratio
    max_h = 7.0*inch
    if img.drawHeight > max_h:
        scale = max_h / img.drawHeight
        img.drawHeight *= scale
        img.drawWidth *= scale
    return KeepTogether([img, Spacer(1, 5), p(caption, "Smallx")])

def header_footer(canvas, doc):
    canvas.saveState()
    w, h = letter
    if doc.page > 1:
        canvas.setStrokeColor(colors.HexColor("#CDD9E2"))
        canvas.line(0.65*inch, h-0.52*inch, w-0.65*inch, h-0.52*inch)
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(GRAY)
        canvas.drawString(0.65*inch, h-0.40*inch, "Exploratory Data Analysis of EV Charging Patterns")
        canvas.drawRightString(w-0.65*inch, 0.42*inch, f"Page {doc.page}")
    canvas.restoreState()

doc = SimpleDocTemplate(str(OUT), pagesize=letter, rightMargin=0.65*inch, leftMargin=0.65*inch,
                        topMargin=0.70*inch, bottomMargin=0.65*inch,
                        title="Exploratory Data Analysis of Electric Vehicle Charging Patterns",
                        author="University Data Science Project")
story = []

# Cover
story += [Spacer(1, 1.0*inch), p("Exploratory Data Analysis of<br/>Electric Vehicle Charging Patterns", "ReportTitle"),
          p("City of Palo Alto Electric Vehicle Charging Station Usage<br/>July 2011 - December 2020", "Subtitle"),
          Spacer(1, 0.25*inch)]
cover_data = [
    ["Original dataset", "259,415 sessions x 33 variables"],
    ["Cleaned dataset", "259,295 sessions"],
    ["Date coverage", "July 29, 2011 - December 31, 2020"],
    ["Unique stations", "47"],
    ["Analysis", "Descriptive statistics, temporal patterns, station comparisons, idle behavior, outliers, correlations, and optional clustering"],
]
t = Table(cover_data, colWidths=[1.55*inch, 4.9*inch], hAlign="CENTER")
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (0,-1), NAVY), ("TEXTCOLOR", (0,0), (0,-1), colors.white),
    ("FONTNAME", (0,0), (0,-1), "Helvetica-Bold"), ("FONTNAME", (1,0), (1,-1), "Helvetica"),
    ("FONTSIZE", (0,0), (-1,-1), 9), ("LEADING", (0,0), (-1,-1), 12),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"), ("ROWBACKGROUNDS", (1,0), (1,-1), [colors.white, LIGHT]),
    ("GRID", (0,0), (-1,-1), 0.4, colors.HexColor("#B8CBD8")), ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7)
]))
story += [t, Spacer(1, 0.35*inch), p("This report summarizes results calculated by the fully executed Jupyter notebook. Statistical outliers were investigated rather than automatically removed, and all relationships are interpreted as associations rather than causal effects.", "Callout"), PageBreak()]

story += [p("Executive Summary", "H1x")]
for x in [
    "The cleaned data contain <b>259,295 charging sessions</b> and <b>2,215,029.06 kWh</b> of delivered energy.",
    "Sessions most often started at <b>11:00 AM</b>. Wednesday was the busiest day of the week, and January was the busiest calendar month.",
    "Average energy was <b>8.54 kWh per session</b>; median energy was <b>6.87 kWh</b>.",
    "Average active charging time was <b>2.00 hours</b>; median active charging time was <b>1.82 hours</b>.",
    "Charging duration and energy delivered had a strong positive correlation of <b>r = 0.871</b>, but long sessions did not always deliver unusually high energy.",
    "Weekdays accounted for <b>76.1%</b> of sessions.",
    "Mean idle time was <b>0.49 hours</b>, and <b>12.1%</b> of sessions had at least one hour of post-charging idle connection time.",
    "The busiest station was <b>PALO ALTO CA / HAMILTON #2</b> with <b>23,706 sessions</b>.",
]: story.append(bullet(x))

story += [p("Dataset and Cleaning", "H1x"), p("The source contains timestamps, total connection duration, active charging time, energy, station and location information, fees, port and plug types, coordinates, and equipment/event identifiers. The analysis automatically identified the relevant columns from the actual schema.")]
clean_table = [
    ["Measure", "Value"], ["Original records", "259,415"], ["Removed records", "120"], ["Final records", "259,295"],
    ["Total energy", "2,215,029.06 kWh"], ["Unique stations", "47"]
]
t = Table(clean_table, colWidths=[3.1*inch, 2.2*inch])
t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),NAVY),("TEXTCOLOR",(0,0),(-1,0),colors.white),("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),("GRID",(0,0),(-1,-1),0.4,colors.HexColor("#B8CBD8")),("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white,LIGHT]),("FONTSIZE",(0,0),(-1,-1),9),("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6)]))
story += [t, Spacer(1, 8), p("Cleaning removed exact duplicates and records with objectively invalid timestamps, negative energy, non-positive durations, or active charging time materially longer than total connection time. Missing descriptive fields did not cause removal when the session remained analytically usable. Valid extreme values were retained for outlier analysis."), PageBreak()]

story += [p("Research Question 1: When Are Chargers Used Most?", "H1x"), figure("charging_sessions_by_time.png", "Figure 1. Session counts by hour, day of week, calendar month, and weekday/weekend classification.", 7.05*inch), Spacer(1,8), p("The busiest session start hour was <b>11:00 AM</b>, the busiest day was <b>Wednesday</b>, and the busiest calendar month was <b>January</b>. Weekday activity dominated, accounting for 76.1% of all cleaned sessions. These figures measure recorded use, not unmet demand or queueing.") , PageBreak()]

story += [p("Research Question 2: How Did Usage Change Over Time?", "H1x"), figure("monthly_charging_trend.png", "Figure 2. Monthly session count, total energy, average energy per session, and average charging duration.", 7.0*inch), Spacer(1,8), p("The busiest observed year was <b>2017</b> with <b>48,950 sessions</b>. The busiest individual month was <b>May 2017</b> with <b>4,982 sessions</b>. Calendar year 2011 contains only six months and should not be compared directly with full years. Changes over time are descriptive and do not establish effects from EV adoption, infrastructure additions, policy, or the pandemic."), PageBreak()]

story += [p("Research Question 3: Charging Duration and Energy", "H1x"), figure("duration_vs_energy.png", "Figure 3. Charging duration versus energy delivered. The displayed axes are limited to the 99th percentiles for readability.", 7.0*inch), Spacer(1,8), p("The Pearson correlation was <b>r = 0.871</b>, indicating a strong positive linear association. Longer active charging generally coincided with more energy, but the longest sessions still showed a range of energy delivery. Correlation does not prove that duration alone causes energy use; vehicle limits, charger power, battery state, interruptions, and equipment differences may also matter."), PageBreak()]

story += [p("Research Question 4: Station Differences", "H1x"), figure("top_charging_stations.png", "Figure 4. Top stations by recorded session count and total delivered energy.", 7.0*inch), Spacer(1,8), p("PALO ALTO CA / HAMILTON #2 was the busiest station with <b>23,706 sessions</b>. Rankings by sessions and total energy are not identical, showing why station activity should be assessed using both volume and energy. The accompanying station summary CSV also reports average and median duration, mean energy, and idle time for every station."), PageBreak()]

story += [p("Research Question 5: Weekday vs Weekend", "H1x"), figure("weekday_weekend_comparison.png", "Figure 5. Weekday/weekend energy, duration, and session start-time profiles.", 7.0*inch), Spacer(1,8), p("Weekend sessions used <b>7.6% less average energy</b> and had <b>14.5% shorter average active charging time</b> than weekday sessions. Weekday and weekend start-time profiles also differ. These are unadjusted comparisons and may partly reflect different station mixes or years."), PageBreak()]

story += [p("Research Question 6: Seasonal Patterns", "H1x"), figure("seasonal_charging_patterns.png", "Figure 6. Recorded sessions and average energy per session by meteorological season.", 7.0*inch), Spacer(1,8), p("Winter had both the highest total session count and the highest average energy per session. Seasonal totals combine multiple years and are affected by growth in the charging network and partial-year coverage. The pattern therefore should not be attributed to weather without additional evidence."), PageBreak()]

story += [p("Research Question 7: Occupancy and Idle Behavior", "H1x"), figure("idle_time_distribution.png", "Figure 7. Distribution of idle time, limited to the 99th percentile for readability.", 7.0*inch), Spacer(1,8), p("Idle time was defined as total connection time minus active charging time. The average was <b>0.49 hours</b>, while the median was only <b>0.01 hours</b>, indicating a right-skewed distribution. Using an analytical threshold of one hour, <b>12.1%</b> of sessions had substantial idle time. This threshold is not an official operating standard."), Spacer(1,10), figure("stations_highest_idle_time.png", "Figure 8. Stations with the highest average idle time among stations with at least 100 sessions.", 6.8*inch), PageBreak()]

story += [p("Outliers and Correlations", "H1x"), figure("outlier_boxplots.png", "Figure 9. Box plots for energy, active charging duration, and energy per active charging hour.", 7.0*inch), Spacer(1,8), p("IQR and percentile methods flagged unusual sessions for review. Outlier status alone was not treated as evidence of bad data. Extreme values could represent overnight parking, interrupted charging, different charger power, high-capacity vehicles, or logging anomalies."), Spacer(1,12), figure("correlation_heatmap.png", "Figure 10. Correlations among meaningful continuous variables. Numeric identifiers were deliberately excluded.", 6.4*inch), PageBreak()]

story += [p("Optional Clustering", "H1x"), figure("optional_clustering_diagnostics.png", "Figure 11. Elbow and silhouette diagnostics for exploratory K-means clustering.", 7.0*inch), Spacer(1,8), p("K-means was included only as a small exploratory extension. Features were standardized, and extreme values were winsorized for clustering stability without modifying the cleaned dataset. Clusters were interpreted using their observed feature statistics rather than speculative labels such as commuter or heavy user."),
          p("Limitations", "H1x")]
for x in [
    "The dataset represents one geographic area and charging-network context.",
    "Observational data cannot establish causation.",
    "Station inventory, equipment, pricing, and policies may have changed over time.",
    "The first year contains only six months of observations.",
    "Missing descriptive fields limit some user- and equipment-level analyses.",
    "Valid outliers may reflect real behavior or unrecognized logging problems.",
    "The data do not directly measure queues, unmet demand, trip purpose, battery state of charge, or user intent.",
]: story.append(bullet(x))
story += [p("Conclusion", "H1x"), p("Palo Alto charging behavior varies materially by time, station, and day type. Energy and active charging duration move together, while total connection time additionally captures post-charging occupancy. The findings show that session count, energy, active charging duration, and idle time should be considered together. They provide a detailed descriptive account of observed use but do not support causal claims."),
          Spacer(1,10), p("Project files", "H2x"), p("The executed notebook, cleaned data, summary CSV files, figures, and PROJECT_RESULTS.md are stored in the same Desktop/next project folder.", "Smallx")]

doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print(OUT)
