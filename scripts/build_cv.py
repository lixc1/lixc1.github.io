"""Build the website CV with ReportLab. Content updated September 2026."""
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib.pagesizes import letter

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/files/CV_Xincheng_Li.pdf'
OUT.parent.mkdir(parents=True, exist_ok=True)
green = colors.HexColor('#214b41')
styles = {
    'body': ParagraphStyle('body', fontName='Helvetica', fontSize=10, leading=13, spaceAfter=6),
    'title': ParagraphStyle('title', fontName='Helvetica-Bold', fontSize=25, leading=30, textColor=green, spaceAfter=9),
    'section': ParagraphStyle('section', fontName='Helvetica-Bold', fontSize=13, leading=17, textColor=green, spaceBefore=10, spaceAfter=7, keepWithNext=True),
    'entry': ParagraphStyle('entry', fontName='Helvetica-Bold', fontSize=10.5, leading=14, spaceAfter=4, keepWithNext=True),
    'meta': ParagraphStyle('meta', fontName='Helvetica', fontSize=9, leading=12, textColor=colors.HexColor('#555555'), spaceAfter=7),
}
story = []
def p(text, style='body'):
    story.append(Paragraph(text, styles[style]))
def section(text): p(text, 'section')
def entry(title, detail):
    p(title, 'entry')
    p(detail)
def link(url, label): return f'<a href="{url}" color="#214b41">{label}</a>'

p('Xincheng Li', 'title')
p('Ph.D. in Electrical Engineering | Autonomous systems, human-robot interaction, control &amp; perception', 'meta')
p('8233 Styers Ct, Laurel, MD 20723 | 443-251-9297<br/>' + link('mailto:lixc1sc@gmail.com', 'lixc1sc@gmail.com') + ' | ' + link('https://lixc1.github.io', 'lixc1.github.io'), 'meta')
section('Professional Summary')
p('Ph.D. in Electrical Engineering with interdisciplinary experience in motion control, robotics, and optimal trajectory generation for robotic systems modeled on Lie groups. Expertise in mathematical modeling, embedded systems, and control algorithm development. Proficient in MATLAB, Python, C++, and Simulink, with practical experience integrating software and hardware for teleoperated and autonomous systems. Research interests include intelligent robotic platforms that enable productive human-machine interaction and safety.')
section('Current Appointment')
entry('Postdoctoral Scholar | University of South Florida', 'Department of Mechanical and Aerospace Engineering. Working with Professor Udit Halder on geometric control, collective motion, and soft robotic grasping.')
section('Education')
entry('University of Maryland, College Park | A. James Clark School of Engineering', '<b>Ph.D., Electrical Engineering</b>, May 2025 | GPA: 3.7<br/>Advisor: Professor P. S. Krishnaprasad')
entry('University of Maryland, College Park | A. James Clark School of Engineering', '<b>B.S., Electrical Engineering; Minor in Physics</b>, May 2018<br/>Cum Laude | GPA: 3.9')
section('Publications &amp; Dissertation')
p('<b>Xincheng Li</b>, Tengyue Liu, and Udit Halder. "On Feedback Speed Control for a Planar Tracking." <i>IEEE Control Systems Letters</i>, 2026.<br/>' + link('https://doi.org/10.1109/LCSYS.2026.3708578', 'doi:10.1109/LCSYS.2026.3708578') + ' | ' + link('https://arxiv.org/abs/2604.09795', 'arXiv:2604.09795'))
p('Udit Halder, Nicolas Echeverria Zambrano, and <b>Xincheng Li</b>. "Kinematics of continuum planar grasping." <i>IEEE Conference on Decision and Control (CDC)</i>, 2026. <b>Accepted.</b><br/>' + link('https://arxiv.org/abs/2604.09800', 'arXiv:2604.09800'))
p('<b>Xincheng Li</b>. <i>Symmetry and Motion: Geometric Control of Human Agents.</i> Ph.D. dissertation, University of Maryland, College Park, 2025.<br/>' + link('https://doi.org/10.13016/rglm-vbqv', 'doi:10.13016/rglm-vbqv'))

story.append(PageBreak())
section('Research Experience')
entry('Intelligent Servosystems Laboratory | Institute for Systems Research', 'University of Maryland, College Park, MD<br/><b>Graduate Research Assistant | Summer 2019 - Summer 2025</b>')
p('Designed time-optimal controllers for Hilare-type mobile robots using the Pontryagin Maximum Principle and Lie-Poisson reduction, reducing trajectory search space and computational load.')
p('Developed a curvature-minimizing control strategy for robotic platforms; validated the system using MATLAB and symbolic simulation.')
p('Modeled human-robot interaction for obstacle avoidance using VICON motion capture data, applying signal processing and shape reconstruction to filter noisy data. Analyzed trajectory adherence to the two-thirds power law associated with affine geometry in motion.')
p('<b>Dissertation research:</b> Motion modeling and control for single- and multi-agent systems using the equi-affine group SA(2). The work connects the two-thirds power law of human movement with its abstraction in matrix Lie groups.')
p('Related research topics with P. S. Krishnaprasad and Eric Justh:<br/>- The two-thirds power law and optimal control on Lie groups<br/>- The two-thirds power law and control of interacting human agents', 'meta')
entry('Visual Analytics Laboratory | Institute for Physical Sciences and Technology', 'University of Maryland, College Park, MD<br/><b>Undergraduate Research Assistant | Summer 2016</b>')
p('Built OpenCV object detection pipelines for real-time segmentation. Developed 2D-to-depth estimation algorithms and integrated IBM Bluemix and Azure cloud computing tools for scalability. Investigated CNN-based methods for semantic image segmentation.')
section('Industry Experience')
entry('MathWorks | Natick, MA', '<b>Academic Disciplines Intern | Summer 2022</b>')
p('Developed interactive MATLAB Live Script modules on moving frames and natural Frenet frames, with educational animations explaining differential geometry concepts in robotics. Worked across academic and product teams to iterate on and deploy the final content.')
section('Teaching &amp; Mentoring')
entry('University of Maryland | Department of Electrical and Computer Engineering', '<b>Teaching Assistant, Senior Capstone Design | 2024-2025</b> (fall and spring)')
p('Co-led ENEE408I, focused on full-stack integration of robotic systems for real-world tasks. Guided autonomous robot development using ROS, C++, ESP32 microcontrollers, and TurtleBot platforms. Taught real-time computer vision using YOLO and OpenCV for detection, recognition, and navigation.')
p('Supervised system integration, including communication protocols, sensor data fusion, and control algorithms. Mentored teams from concept to final demonstrations, emphasizing robust architecture and engineering rigor. Collaborated with faculty on curriculum and hardware/software co-design challenges.')
p('Mentored two undergraduate researchers in the Intelligent Servosystems Laboratory studying the two-thirds power law in human locomotion using VICON motion capture.')

story.append(PageBreak())
section('Technical Skills')
p('<b>Hardware:</b> Analog/digital circuit design; FPGA; Arduino; embedded systems; feedback and servo control systems design.<br/><b>Software:</b> AutoCAD, MIPS, Verilog, PSpice, Xilinx; Python, MATLAB/Simulink, C/C++; VICON Nexus/Tracker, ROS, OpenCV, Git.')
section('Selected Projects')
entry('Generative Adversarial Neural Network | Fall 2017', 'University of Maryland, Department of Electrical and Computer Engineering')
p('Implemented a PyTorch GAN to generate MRI scan modalities for glioblastoma patients. Adapted GAN algorithms by training generators for each modality and enforcing pixel-wise loss. Gathered and labeled training data from ImageNet using heuristic algorithms and fitted the dataset using histogram methods.')
entry('AI-Powered Chat Agent | Independent Project, 2023 - Present', 'Real-time assistant for server management')
p('Developed a local Python chat agent integrating a fine-tuned large language model for natural language interaction and task handling. Implemented message parsing, context handling, and response generation, with modular command, memory, and query handling. Optimized token management, prompting, and asynchronous processing for multiple users. Experimented with retrieval-augmented architectures using local vector stores.')
section('Leadership &amp; Teamwork')
entry('Gemstone Honors Program, Team ARMIT | College Park, MD', '<b>Virtual Reality Sub-team Leader | 2014-2018</b>')
p('Led development of a virtual reality UAV control interface within a multidisciplinary team of 12 students. Designed a Unity stereoscopic acuity test to evaluate immersive user performance. Built synchronized dual-GoPro video streaming to an Oculus Rift headset and a custom control system for teleoperating a 3D-printed gimbal.')
p('Co-authored and presented a 30-page research proposal that earned first place at the FedCentric Cybersecurity Competition during the Gemstone Junior Colloquium. Managed team finances and procurement as financial liaison.')
entry('Terp Development and Consulting Club | College Park, MD', '<b>Mic-Sense Sub-team | 2016-2017</b>')
p('Worked with McKeldin Library staff on a sensor-based traffic monitoring system to estimate floor-level occupancy. Developed a low-pass filter to reduce environmental sensor noise and improve signal accuracy. Participated in client meetings to iterate on the prototype and deliver a functional proof of concept.')
section('Awards')
p('<b>2024-2025</b> | ECE Outstanding Teaching Assistant<br/><b>2018</b> | AIAA Student Conference, First Place<br/><b>2016</b> | FedCentric Cybersecurity Award<br/><b>2014-2018</b> | Dean\'s List, University of Maryland')

def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor('#ccd4d0'))
    canvas.line(48, 42, 564, 42)
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(colors.HexColor('#555555'))
    canvas.drawString(48, 28, 'Xincheng Li | Curriculum Vitae | Updated September 2026')
    canvas.drawRightString(564, 28, str(doc.page))
    canvas.restoreState()

doc = SimpleDocTemplate(str(OUT), pagesize=letter, rightMargin=48, leftMargin=48,
                        topMargin=38, bottomMargin=55, title='Xincheng Li - Curriculum Vitae', author='Xincheng Li')
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUT)
