from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.platypus.flowables import HRFlowable
from reportlab.lib.colors import HexColor, white, black

# ── Palette ──────────────────────────────────────────────
PRIMARY   = HexColor('#1d4ed8')
PRIMARY_L = HexColor('#dbeafe')
DARK      = HexColor('#111827')
GRAY      = HexColor('#6b7280')
GRAY_L    = HexColor('#f3f4f6')
GRAY_B    = HexColor('#e5e7eb')
SUCCESS   = HexColor('#16a34a')
SUCCESS_L = HexColor('#dcfce7')
WARNING   = HexColor('#d97706')
WARNING_L = HexColor('#fef3c7')
DANGER    = HexColor('#dc2626')
DANGER_L  = HexColor('#fee2e2')
CODE_BG   = HexColor('#1e1e2e')
CODE_FG   = HexColor('#cdd6f4')
TEAL      = HexColor('#0d9488')
TEAL_L    = HexColor('#ccfbf1')
W, H      = A4

# ── Styles ────────────────────────────────────────────────
styles = getSampleStyleSheet()

def s(name, **kw):
    return ParagraphStyle(name, **kw)

ST = {
    'h1': s('H1', fontSize=26, leading=32, textColor=DARK,
             fontName='Helvetica-Bold', spaceAfter=6),
    'h2': s('H2', fontSize=16, leading=22, textColor=PRIMARY,
             fontName='Helvetica-Bold', spaceBefore=14, spaceAfter=6),
    'h3': s('H3', fontSize=12, leading=17, textColor=DARK,
             fontName='Helvetica-Bold', spaceBefore=10, spaceAfter=4),
    'body': s('Body', fontSize=10, leading=16, textColor=DARK,
              fontName='Helvetica', spaceAfter=4),
    'body_gray': s('BodyGray', fontSize=10, leading=16, textColor=GRAY,
                   fontName='Helvetica', spaceAfter=4),
    'code': s('Code', fontSize=9, leading=14, textColor=CODE_FG,
              fontName='Courier', backColor=CODE_BG,
              leftIndent=10, rightIndent=10, spaceBefore=4, spaceAfter=4,
              borderPadding=(6,8,6,8)),
    'caption': s('Caption', fontSize=8, leading=12, textColor=GRAY,
                 fontName='Helvetica', spaceAfter=2, alignment=TA_CENTER),
    'badge': s('Badge', fontSize=8, leading=12, textColor=white,
               fontName='Helvetica-Bold', alignment=TA_CENTER),
    'step': s('Step', fontSize=10, leading=15, textColor=DARK,
              fontName='Helvetica', leftIndent=20, spaceAfter=3),
    'bullet': s('Bullet', fontSize=10, leading=15, textColor=DARK,
                fontName='Helvetica', leftIndent=16, spaceAfter=3),
    'sub': s('Sub', fontSize=9, leading=13, textColor=GRAY,
             fontName='Helvetica', leftIndent=32, spaceAfter=2),
    'title_hero': s('TitleHero', fontSize=32, leading=40, textColor=white,
                    fontName='Helvetica-Bold', alignment=TA_CENTER),
    'sub_hero': s('SubHero', fontSize=13, leading=20, textColor=HexColor('#bfdbfe'),
                  fontName='Helvetica', alignment=TA_CENTER),
    'label': s('Label', fontSize=8, leading=12, textColor=GRAY,
               fontName='Helvetica-Bold', letterSpacing=0.5),
    'timeline_time': s('TLTime', fontSize=9, leading=13, textColor=PRIMARY,
                       fontName='Helvetica-Bold', alignment=TA_RIGHT),
    'timeline_title': s('TLTitle', fontSize=10, leading=14, textColor=DARK,
                        fontName='Helvetica-Bold'),
    'timeline_body': s('TLBody', fontSize=9, leading=13, textColor=GRAY,
                       fontName='Helvetica'),
    'tag': s('Tag', fontSize=8, leading=11, textColor=PRIMARY,
             fontName='Helvetica-Bold', alignment=TA_CENTER),
}

# ── Helper builders ───────────────────────────────────────
def hr(color=GRAY_B, thickness=0.8):
    return HRFlowable(width='100%', thickness=thickness, color=color,
                      spaceAfter=4, spaceBefore=4)

def sp(h=4):
    return Spacer(1, h)

def chip(text, bg=PRIMARY, fg=white, w=None):
    style = ParagraphStyle('chip', fontSize=8, leading=11, textColor=fg,
                           fontName='Helvetica-Bold', alignment=TA_CENTER)
    cell = [[Paragraph(text, style)]]
    ts = TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg),
        ('ROWBACKGROUNDS', (0,0), (-1,-1), [bg]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('ROUNDEDCORNERS', [4,4,4,4]),
    ])
    return Table(cell, colWidths=[w or 60], style=ts)

def info_box(title, lines, bg=PRIMARY_L, border=PRIMARY, icon=''):
    content = [Paragraph(f'<b>{icon} {title}</b>', ParagraphStyle(
        'ibt', fontSize=10, leading=14, textColor=border,
        fontName='Helvetica-Bold', spaceAfter=3))]
    for l in lines:
        content.append(Paragraph(f'• {l}', ParagraphStyle(
            'ibb', fontSize=9, leading=13, textColor=DARK,
            fontName='Helvetica', leftIndent=6)))
    t = Table([[content]], colWidths=[W - 40*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LINEAFTER', (0,0), (0,-1), 3, border),
        ('ROUNDEDCORNERS', [6,6,6,6]),
    ]))
    return t

def section_header(text, color=PRIMARY):
    t = Table([[Paragraph(text, ParagraphStyle(
        'sh', fontSize=13, leading=18, textColor=white,
        fontName='Helvetica-Bold'))]],
        colWidths=[W - 40*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), color),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 14),
        ('ROUNDEDCORNERS', [6,6,6,6]),
    ]))
    return t

def two_col(left_content, right_content, left_w=None):
    lw = left_w or (W - 40*mm) * 0.55
    rw = (W - 40*mm) - lw
    t = Table([[left_content, right_content]], colWidths=[lw, rw])
    t.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    return t

def code_block(lines):
    joined = '<br/>'.join(lines)
    return Paragraph(joined, ST['code'])

def timeline_row(time, title, bullets):
    time_cell = [Paragraph(time, ST['timeline_time'])]
    content_cell = [Paragraph(title, ST['timeline_title'])]
    for b in bullets:
        content_cell.append(Paragraph(f'↳ {b}', ST['timeline_body']))
    t = Table([[time_cell, content_cell]], colWidths=[18*mm, (W-40*mm)-20*mm])
    t.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LINEAFTER', (0,0), (0,-1), 2, PRIMARY_L),
    ]))
    return t

# ── Page template (header/footer) ────────────────────────
def on_page(canvas, doc):
    canvas.saveState()
    # Top accent line
    canvas.setFillColor(PRIMARY)
    canvas.rect(0, H - 4, W, 4, fill=1, stroke=0)
    # Footer
    canvas.setFillColor(GRAY_B)
    canvas.rect(0, 0, W, 18, fill=1, stroke=0)
    canvas.setFillColor(GRAY)
    canvas.setFont('Helvetica', 8)
    canvas.drawString(20*mm, 6, 'GesUsers2 — Projet Java EE | Gestion des Utilisateurs')
    canvas.drawRightString(W - 20*mm, 6, f'Page {doc.page}')
    canvas.restoreState()

def on_first_page(canvas, doc):
    canvas.saveState()
    # Full blue hero background
    canvas.setFillColor(PRIMARY)
    canvas.rect(0, H - 110*mm, W, 110*mm, fill=1, stroke=0)
    # Decorative circles
    canvas.setFillColor(HexColor('#1e40af'))
    canvas.circle(W - 30*mm, H - 20*mm, 60, fill=1, stroke=0)
    canvas.setFillColor(HexColor('#2563eb'))
    canvas.circle(25*mm, H - 80*mm, 35, fill=1, stroke=0)
    # Bottom footer
    canvas.setFillColor(GRAY_B)
    canvas.rect(0, 0, W, 18, fill=1, stroke=0)
    canvas.setFillColor(GRAY)
    canvas.setFont('Helvetica', 8)
    canvas.drawString(20*mm, 6, 'GesUsers2 — Projet Java EE | Gestion des Utilisateurs')
    canvas.drawRightString(W - 20*mm, 6, 'Page 1')
    canvas.restoreState()

# ── Document ──────────────────────────────────────────────
OUTPUT = r'C:\Users\DELL\Downloads\jee\workspace\gesusers2\guide_presentation.pdf'
doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    leftMargin=20*mm, rightMargin=20*mm,
    topMargin=14*mm, bottomMargin=14*mm,
    title='GesUsers2 — Guide de Présentation',
    author='Salif Biaye',
    subject='Projet Académique Java EE',
)

story = []

# ═══════════════════════════════════════════════════════════
# PAGE 1 — COVER
# ═══════════════════════════════════════════════════════════
story.append(Spacer(1, 62*mm))
story.append(Paragraph('GesUsers2', ST['title_hero']))
story.append(sp(6))
story.append(Paragraph('Gestion des Utilisateurs — Projet Académique Java EE', ST['sub_hero']))
story.append(sp(8))

# Tags row
tags = ['Java EE', 'MVC', 'DAO Pattern', 'Servlet', 'JSP', 'MySQL', 'Docker', 'Rôles Admin/User']
tag_cells = [[chip(t, bg=HexColor('#1e40af'), w=None) for t in tags]]
tag_table = Table([tag_cells[0]], colWidths=[None]*len(tags))
tag_table.setStyle(TableStyle([
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('LEFTPADDING', (0,0), (-1,-1), 3),
    ('RIGHTPADDING', (0,0), (-1,-1), 3),
]))
story.append(tag_table)
story.append(sp(10))
story.append(Paragraph('Salif Biaye  ·  2025  ·  Tomcat 11 · Jakarta EE 6', ST['sub_hero']))

story.append(Spacer(1, 42*mm))

# Quick stats cards
stats = [
    ('7', 'Servlets\n& Filtres'),
    ('3', 'Couches\n(MVC)'),
    ('2', 'Rôles\nAdmin / User'),
    ('2', 'Thèmes\nLight / Dark'),
    ('5', 'Patterns\nDe conception'),
]
stat_data = []
for val, label in stats:
    cell = [
        Paragraph(f'<b>{val}</b>', ParagraphStyle('sv', fontSize=22, leading=26,
            textColor=PRIMARY, fontName='Helvetica-Bold', alignment=TA_CENTER)),
        Paragraph(label.replace('\n','<br/>'), ParagraphStyle('sl', fontSize=8, leading=11,
            textColor=GRAY, fontName='Helvetica', alignment=TA_CENTER)),
    ]
    stat_data.append(cell)

stats_table = Table([stat_data], colWidths=[(W-40*mm)/5]*5)
stats_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), GRAY_L),
    ('TOPPADDING', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ('LEFTPADDING', (0,0), (-1,-1), 4),
    ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ('LINEBEFORE', (1,0), (-1,-1), 1, GRAY_B),
    ('ROUNDEDCORNERS', [8,8,8,8]),
]))
story.append(stats_table)

story.append(PageBreak())

# ═══════════════════════════════════════════════════════════
# PAGE 2 — ARCHITECTURE
# ═══════════════════════════════════════════════════════════
story.append(section_header('PARTIE 1 — Architecture Technique  (2 min)'))
story.append(sp(10))

story.append(Paragraph('Architecture 3 Tiers', ST['h2']))
story.append(Paragraph(
    'L\'application suit un modèle MVC strict avec une séparation en 3 couches indépendantes.',
    ST['body']))
story.append(sp(6))

# 3-tier diagram as table
tier_data = [
    [Paragraph('<b>① Présentation</b>', ParagraphStyle('th', fontSize=10, leading=14,
               textColor=white, fontName='Helvetica-Bold', alignment=TA_CENTER)),
     Paragraph('Servlets (Controllers) + JSP (Views)', ParagraphStyle('td', fontSize=9,
               leading=13, textColor=DARK, fontName='Helvetica'))],
    [Paragraph('<b>② Métier</b>', ParagraphStyle('th', fontSize=10, leading=14,
               textColor=white, fontName='Helvetica-Bold', alignment=TA_CENTER)),
     Paragraph('UserService · AuthenticationService · Form Validation', ParagraphStyle(
               'td', fontSize=9, leading=13, textColor=DARK, fontName='Helvetica'))],
    [Paragraph('<b>③ Données</b>', ParagraphStyle('th', fontSize=10, leading=14,
               textColor=white, fontName='Helvetica-Bold', alignment=TA_CENTER)),
     Paragraph('UtilisateurDaoBdd (MySQL JDBC) · UtilisateurDao (in-memory)', ParagraphStyle(
               'td', fontSize=9, leading=13, textColor=DARK, fontName='Helvetica'))],
]
tier_table = Table(tier_data, colWidths=[45*mm, (W-40*mm)-47*mm])
tier_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (0,0), PRIMARY),
    ('BACKGROUND', (0,1), (0,1), HexColor('#059669')),
    ('BACKGROUND', (0,2), (0,2), HexColor('#7c3aed')),
    ('BACKGROUND', (1,0), (1,0), HexColor('#eff6ff')),
    ('BACKGROUND', (1,1), (1,1), HexColor('#f0fdf4')),
    ('BACKGROUND', (1,2), (1,2), HexColor('#f5f3ff')),
    ('TOPPADDING', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
    ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ('ROWBACKGROUNDS', (0,0), (-1,-1), [None]),
    ('GRID', (0,0), (-1,-1), 0.5, white),
    ('ROUNDEDCORNERS', [6,6,6,6]),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
]))
story.append(tier_table)
story.append(sp(14))

# Design patterns
story.append(Paragraph('Patterns de Conception', ST['h2']))
patterns = [
    ('MVC', 'Séparation Modèle-Vue-Contrôleur : Servlet = Controller, JSP = View, Bean = Model', PRIMARY, PRIMARY_L),
    ('DAO', 'Data Access Object : abstraction de la couche BDD, 2 implémentations interchangeables', HexColor('#059669'), SUCCESS_L),
    ('Service Layer', 'Logique métier encapsulée dans UserService et AuthenticationService', HexColor('#7c3aed'), HexColor('#f5f3ff')),
    ('Filter Pattern', 'AuthenticationFilter intercepte toutes les routes protégées, vérifie session + rôle', HexColor('#d97706'), WARNING_L),
    ('Strategy', 'UtilisateurDao (in-memory) vs UtilisateurDaoBdd (MySQL) — même interface, swap transparent', TEAL, TEAL_L),
]
for name, desc, color, light in patterns:
    row = Table([[
        Paragraph(name, ParagraphStyle('pn', fontSize=9, leading=12, textColor=color,
                  fontName='Helvetica-Bold', alignment=TA_CENTER)),
        Paragraph(desc, ParagraphStyle('pd', fontSize=9, leading=13, textColor=DARK,
                  fontName='Helvetica')),
    ]], colWidths=[28*mm, (W-40*mm)-30*mm])
    row.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), light),
        ('BACKGROUND', (1,0), (1,0), GRAY_L),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('LINEBEFORE', (0,0), (0,-1), 3, color),
        ('GRID', (0,0), (-1,-1), 0.3, GRAY_B),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(row)
    story.append(sp(3))

story.append(PageBreak())

# ═══════════════════════════════════════════════════════════
# PAGE 3 — STRUCTURE DU PROJET
# ═══════════════════════════════════════════════════════════
story.append(section_header('Structure du Projet & Code Clé'))
story.append(sp(10))

story.append(Paragraph('Arborescence', ST['h2']))
tree_lines = [
    'gesusers2/',
    '├── src/main/java/',
    '│   ├── beans/          → Utilisateur.java  (id, nom, prenom, login, password, role)',
    '│   ├── dao/            → UtilisateurDao.java (in-memory) · UtilisateurDaoBdd.java (MySQL)',
    '│   ├── service/        → UserService.java · AuthenticationService.java',
    '│   ├── web/controller/ → AddUserServlet · UpdateUserServlet · RemoveUserServlet',
    '│   │                     ListUserServlet · AuthenticationController · ThemeController',
    '│   ├── web/form/       → AbstractUserForm · AddUserForm · UpdateUserForm',
    '│   ├── mapper/         → UserMapper.java  (Form ↔ Bean)',
    '│   └── filter/         → AuthenticationFilter.java',
    '├── src/main/webapp/',
    '│   ├── WEB-INF/        → login.jsp · listerUtilisateurs.jsp · ajouterUtilisateur.jsp',
    '│   │                     modifierUtilisateur.jsp · web.xml',
    '│   ├── inc/            → header.jsp · footer.jsp  (layout partagé)',
    '│   └── css/            → light/ · dark/  (design.css · header.css · footer.css)',
    '├── init.sql            → Schéma BDD + données de test',
    '├── docker-compose.yml  → MySQL + Adminer',
    '└── build.xml           → Ant compile · war · deploy',
]
story.append(code_block(tree_lines))
story.append(sp(12))

# Bean + DAO
story.append(Paragraph('Bean Utilisateur — Modèle', ST['h2']))
story.append(code_block([
    '<font color="#6272a4">// beans/Utilisateur.java</font>',
    '<font color="#ff79c6">public class</font> <font color="#50fa7b">Utilisateur</font> {',
    '    <font color="#ff79c6">private</font> <font color="#8be9fd">int</font> id;',
    '    <font color="#ff79c6">private</font> <font color="#8be9fd">String</font> nom, prenom, login, password;',
    '    <font color="#ff79c6">private</font> <font color="#8be9fd">String</font> <font color="#ffb86c">role</font>;  <font color="#6272a4">// "admin" | "user"</font>',
    '    <font color="#6272a4">// constructeurs, getters, setters...</font>',
    '}',
]))
story.append(sp(8))

story.append(Paragraph('DAO MySQL — Couche Données', ST['h2']))
story.append(code_block([
    '<font color="#6272a4">// dao/UtilisateurDaoBdd.java — méthodes clés</font>',
    '<font color="#ff79c6">public boolean</font> <font color="#50fa7b">ajouter</font>(<font color="#8be9fd">Utilisateur</font> u) {',
    '    <font color="#8be9fd">String</font> sql = <font color="#f1fa8c">"INSERT INTO utilisateur(nom,prenom,login,password,role)"</font>',
    '              + <font color="#f1fa8c">" VALUES(?,?,?,?,?)"</font>;',
    '    <font color="#6272a4">// PreparedStatement → protection injection SQL</font>',
    '    pstmt.setString(5, u.getRole());',
    '    ...',
    '}',
    '',
    '<font color="#ff79c6">public</font> <font color="#8be9fd">Utilisateur</font> <font color="#50fa7b">getByLogin</font>(<font color="#8be9fd">String</font> login) {',
    '    <font color="#8be9fd">String</font> sql = <font color="#f1fa8c">"SELECT * FROM utilisateur WHERE login=?"</font>;',
    '    <font color="#6272a4">// utilisé par AuthenticationService</font>',
    '}',
]))

story.append(PageBreak())

# ═══════════════════════════════════════════════════════════
# PAGE 4 — FORMS + FILTER + RÔLES
# ═══════════════════════════════════════════════════════════
story.append(section_header('Validation · Filtre · Gestion des Rôles'))
story.append(sp(10))

story.append(Paragraph('Validation des Formulaires', ST['h2']))
story.append(Paragraph(
    'Toute saisie passe par un objet Form avant d\'atteindre le Service. '
    'AbstractUserForm définit la validation de base, les sous-classes la spécialisent.',
    ST['body']))
story.append(sp(6))
story.append(code_block([
    '<font color="#6272a4">// web/form/AbstractUserForm.java</font>',
    '<font color="#ff79c6">public abstract class</font> <font color="#50fa7b">AbstractUserForm</font> {',
    '    <font color="#ff79c6">protected</font> <font color="#8be9fd">Map</font>&lt;<font color="#8be9fd">String</font>,<font color="#8be9fd">String</font>&gt; errors;',
    '    <font color="#ff79c6">protected</font> <font color="#8be9fd">String</font> nom, prenom, login, password, <font color="#ffb86c">role</font>;',
    '',
    '    <font color="#ff79c6">protected void</font> <font color="#50fa7b">checkEmptyFields</font>() {',
    '        <font color="#ff79c6">if</font> (nom == <font color="#ff79c6">null</font> || nom.isBlank())',
    '            errors.put(<font color="#f1fa8c">"nom"</font>, <font color="#f1fa8c">"Vous devez renseigner ce champ"</font>);',
    '        <font color="#6272a4">// idem prenom, login, password...</font>',
    '    }',
    '    <font color="#ff79c6">public abstract boolean</font> <font color="#50fa7b">isValid</font>();',
    '}',
]))
story.append(sp(10))

story.append(Paragraph('AuthenticationFilter — Protection des Routes', ST['h2']))
story.append(code_block([
    '<font color="#6272a4">// filter/AuthenticationFilter.java</font>',
    '<font color="#50fa7b">@WebFilter</font>({ <font color="#f1fa8c">"/add"</font>, <font color="#f1fa8c">"/list"</font>, <font color="#f1fa8c">"/update"</font>, <font color="#f1fa8c">"/delete"</font> })',
    '<font color="#ff79c6">public class</font> <font color="#50fa7b">AuthenticationFilter</font> ... {',
    '    <font color="#ff79c6">public void</font> <font color="#50fa7b">doFilter</font>(...) {',
    '        <font color="#8be9fd">HttpSession</font> session = httpRequest.getSession(<font color="#ff79c6">false</font>);',
    '',
    '        <font color="#6272a4">// 1. Non connecté → /login</font>',
    '        <font color="#ff79c6">if</font> (session == <font color="#ff79c6">null</font> || session.getAttribute(<font color="#f1fa8c">"isConnected"</font>) == <font color="#ff79c6">null</font>) {',
    '            redirect(<font color="#f1fa8c">"/login"</font>); <font color="#ff79c6">return</font>;',
    '        }',
    '',
    '        <font color="#6272a4">// 2. Vérification rôle pour /add, /update, /delete</font>',
    '        <font color="#8be9fd">String</font> role = (<font color="#8be9fd">String</font>) session.getAttribute(<font color="#f1fa8c">"role"</font>);',
    '        <font color="#ff79c6">if</font> (pathIsAdminOnly && !<font color="#f1fa8c">"admin"</font>.equals(role)) {',
    '            redirect(<font color="#f1fa8c">"/list?message=Accès+refusé&amp;status=error"</font>); <font color="#ff79c6">return</font>;',
    '        }',
    '        chain.doFilter(request, response);',
    '    }',
    '}',
]))
story.append(sp(10))

story.append(Paragraph('Gestion des Rôles Admin / User', ST['h2']))
roles_data = [
    [Paragraph('<b>Fonctionnalité</b>', ST['label']),
     Paragraph('<b>ADMIN</b>', ST['label']),
     Paragraph('<b>USER</b>', ST['label'])],
    ['Voir la liste des utilisateurs', '✓', '✓'],
    ['Ajouter un utilisateur', '✓', '✗'],
    ['Modifier un utilisateur', '✓', '✗'],
    ['Supprimer un utilisateur', '✓', '✗'],
    ['Accès à /add, /update, /delete', '✓', '✗ (redirect)'],
    ['Lien "Ajouter" dans la sidebar', '✓', 'masqué'],
    ['Boutons Modifier/Supprimer', '✓ (affichés)', '✗ (masqués)'],
    ['Session stockée après login', 'role=admin', 'role=user'],
]
col_w = [(W-40*mm)*0.55, (W-40*mm)*0.22, (W-40*mm)*0.22]
role_table = Table(roles_data, colWidths=col_w)
role_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), DARK),
    ('TEXTCOLOR', (0,0), (-1,0), white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('ALIGN', (1,0), (-1,-1), 'CENTER'),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [white, GRAY_L]),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
    ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ('GRID', (0,0), (-1,-1), 0.5, GRAY_B),
    ('TEXTCOLOR', (1,1), (1,-1), SUCCESS),
    ('TEXTCOLOR', (2,1), (2,-1), DANGER),
    ('ROUNDEDCORNERS', [4,4,4,4]),
]))
story.append(role_table)

story.append(PageBreak())

# ═══════════════════════════════════════════════════════════
# PAGE 5 — BDD + DOCKER
# ═══════════════════════════════════════════════════════════
story.append(section_header('Base de Données & Docker', color=HexColor('#059669')))
story.append(sp(10))

story.append(Paragraph('Schéma MySQL', ST['h2']))
story.append(code_block([
    '<font color="#6272a4">-- init.sql</font>',
    '<font color="#ff79c6">CREATE TABLE IF NOT EXISTS</font> <font color="#50fa7b">utilisateur</font> (',
    '    id        <font color="#8be9fd">INT</font> <font color="#ff79c6">PRIMARY KEY AUTO_INCREMENT</font>,',
    '    nom       <font color="#8be9fd">VARCHAR</font>(255),',
    '    prenom    <font color="#8be9fd">VARCHAR</font>(255),',
    '    login     <font color="#8be9fd">VARCHAR</font>(255) <font color="#ff79c6">UNIQUE NOT NULL</font>,',
    '    password  <font color="#8be9fd">VARCHAR</font>(255),',
    '    role      <font color="#8be9fd">VARCHAR</font>(50) <font color="#ff79c6">NOT NULL DEFAULT</font> <font color="#f1fa8c">\'user\'</font>',
    ');',
    '',
    '<font color="#6272a4">-- Données de test</font>',
    '<font color="#ff79c6">INSERT INTO</font> utilisateur (nom, prenom, login, password, role) <font color="#ff79c6">VALUES</font>',
    '    (<font color="#f1fa8c">\'Dupont\'</font>, <font color="#f1fa8c">\'Jean\'</font>,  <font color="#f1fa8c">\'jdupont\'</font>, <font color="#f1fa8c">\'password123\'</font>, <font color="#ffb86c">\'admin\'</font>),',
    '    (<font color="#f1fa8c">\'Martin\'</font>, <font color="#f1fa8c">\'Marie\'</font>, <font color="#f1fa8c">\'mmartin\'</font>, <font color="#f1fa8c">\'password456\'</font>, <font color="#ffb86c">\'user\'</font>),',
    '    (<font color="#f1fa8c">\'Bernard\'</font>,<font color="#f1fa8c">\'Pierre\'</font>,<font color="#f1fa8c">\'pbernard\'</font>,<font color="#f1fa8c">\'password789\'</font>, <font color="#ffb86c">\'user\'</font>);',
]))
story.append(sp(10))

story.append(Paragraph('Docker Compose — MySQL + Adminer', ST['h2']))
story.append(Paragraph(
    'Adminer (interface web) permet de visualiser la base de données en direct '
    'pendant la démo — preuve visuelle du CRUD.',
    ST['body']))
story.append(sp(6))
story.append(code_block([
    '<font color="#6272a4"># docker-compose.yml</font>',
    '<font color="#ff79c6">services</font>:',
    '  <font color="#50fa7b">mysql</font>:',
    '    image: mysql:8.0',
    '    environment:',
    '      MYSQL_DATABASE: gesusers',
    '      MYSQL_ROOT_PASSWORD: passer123',
    '    ports: ["3306:3306"]',
    '',
    '  <font color="#50fa7b">adminer</font>:',
    '    image: adminer:latest',
    '    ports: ["8081:8080"]',
    '    <font color="#6272a4"># Accès: http://localhost:8081</font>',
    '    <font color="#6272a4"># Server: mysql  User: root  Pass: passer123</font>',
]))
story.append(sp(8))

story.append(info_box(
    'Commande démo BDD',
    [
        'docker compose up -d          → lance MySQL + Adminer en arrière-plan',
        'Ouvrir http://localhost:8081  → interface graphique Adminer',
        'Connexion : server=mysql, user=root, password=passer123, db=gesusers',
        'Montrer la table utilisateur avec les colonnes id, nom, prenom, login, password, role',
        'Effectuer une action dans l\'app (ajout) → F5 dans Adminer → nouvelle ligne visible',
    ],
    bg=SUCCESS_L, border=SUCCESS, icon='🐳'))

story.append(PageBreak())

# ═══════════════════════════════════════════════════════════
# PAGE 6 — GUIDE VIDÉO
# ═══════════════════════════════════════════════════════════
story.append(section_header('PARTIE 2 — Guide Vidéo de Présentation  (~5 min)', color=HexColor('#7c3aed')))
story.append(sp(10))

story.append(Paragraph('Checklist avant de démarrer', ST['h3']))
checks = [
    'Tomcat démarré   →   http://localhost:8080/gesusers2/login',
    'docker compose up -d   →   MySQL + Adminer sur :8081',
    'Navigateur en plein écran, zoom 100%',
    'IDE (Eclipse) ouvert sur le projet pour les screenshots de code',
    'GitHub repo ouvert dans un onglet : github.com/ton-compte/gesusers2',
]
for c in checks:
    story.append(Paragraph(f'☐  {c}', ST['step']))
story.append(sp(12))

# Timeline
story.append(Paragraph('Déroulé Chronologique', ST['h2']))
story.append(hr())
story.append(sp(6))

segments = [
    ('0:00 – 0:20', 'Introduction', [
        'Saluer : "Je vais vous présenter GesUsers2, une application Java EE de gestion d\'utilisateurs"',
        'Montrer la page login dans le navigateur',
        'Stack : Java EE · Servlet · JSP · JSTL · MySQL · Docker · Ant',
    ]),
    ('0:20 – 1:00', 'Architecture 3 Tiers  (IDE ouvert)', [
        'Montrer l\'arborescence Eclipse : beans/ dao/ service/ web/controller/ filter/',
        'Expliquer : "Présentation (Servlet/JSP) → Métier (Service) → Données (DAO → MySQL)"',
        'Montrer rapidement Utilisateur.java → le champ role',
        'Montrer AuthenticationFilter.java → protection + vérification rôle',
    ]),
    ('1:00 – 1:40', 'Validation & Formulaires  (code)', [
        'Montrer AbstractUserForm.java → Map errors, checkEmptyFields()',
        'Mentionner AddUserForm et UpdateUserForm qui héritent → pattern Template Method',
        'Montrer UserMapper.java → conversion Form ↔ Bean',
    ]),
    ('1:40 – 2:00', 'DAO & BDD  (code + Adminer)', [
        'Montrer UtilisateurDaoBdd.java → PreparedStatement, getByLogin()',
        'Basculer sur Adminer (localhost:8081) → montrer la table utilisateur',
        'Colonnes visibles : id, nom, prenom, login, password, role',
    ]),
    ('2:00 – 2:30', 'Démo App — Login Admin', [
        'Se connecter : login = jdupont  /  password = password123',
        'Observer sidebar : avatar "JD", nom "Jean Dupont", badge bleu "ADMIN"',
        'Observer : lien "Ajouter un utilisateur" visible, boutons Modifier/Supprimer visibles',
    ]),
    ('2:30 – 3:10', 'Démo CRUD Admin', [
        'Cliquer Ajouter → remplir le formulaire → choisir rôle "Utilisateur" → Valider',
        'Vérifier dans Adminer : nouvelle ligne dans la table (preuve BDD)',
        'Modifier un utilisateur → changer son rôle en admin → Valider',
        'Supprimer un utilisateur → confirmer dans le modal',
    ]),
    ('3:10 – 3:30', 'Toggle Thème Light / Dark', [
        'Cliquer le bouton 🌙 "Mode sombre" → page bascule en dark',
        'Cliquer ☀️ "Mode clair" → retour au light',
        'Préciser : "thème persisté en session, conservé même après logout"',
    ]),
    ('3:30 – 4:00', 'Démo — Login User (accès restreint)', [
        'Se déconnecter → observer la redirection vers /login avec message de succès',
        'Se connecter : login = mmartin  /  password = password456',
        'Observer sidebar : badge gris "USER", lien Ajouter absent',
        'Tenter d\'accéder à /add manuellement → message "Accès refusé"',
        'Liste : boutons Modifier/Supprimer remplacés par "—"',
    ]),
    ('4:00 – 4:20', 'Redirection si déjà connecté', [
        'Rester connecté et taper /login dans la barre d\'adresse',
        'Observer la redirection automatique vers /list',
        'Expliquer : "AuthenticationController vérifie la session en doGet"',
    ]),
    ('4:20 – 5:00', 'GitHub + Conclusion', [
        'Montrer le repo GitHub → code source, README avec screenshot de l\'app',
        'Parcourir rapidement les commits : structure, auth, UI, rôles',
        'Conclure : "Architecture propre, patterns académiques, bonus rôles, déployable avec Docker"',
    ]),
]

for time, title, bullets in segments:
    story.append(timeline_row(time, title, bullets))
    story.append(hr(GRAY_B, 0.5))
    story.append(sp(2))

story.append(PageBreak())

# ═══════════════════════════════════════════════════════════
# PAGE 7 — README + GITHUB
# ═══════════════════════════════════════════════════════════
story.append(section_header('README & GitHub — Check-list finale', color=HexColor('#d97706')))
story.append(sp(10))

story.append(Paragraph('Mise à Jour du README', ST['h2']))
story.append(Paragraph(
    'Avant la présentation, mettre à jour le README.md avec une capture d\'écran de l\'application.',
    ST['body']))
story.append(sp(6))

readme_data = [
    [Paragraph('<b>Section README</b>', ST['label']),
     Paragraph('<b>Contenu à inclure</b>', ST['label'])],
    ['Screenshot', 'Capture de la liste des utilisateurs (light + dark si possible)'],
    ['Stack', 'Java EE · Tomcat 11 · JSP · JSTL · MySQL · Docker · Ant'],
    ['Fonctionnalités', 'CRUD, Auth, Rôles admin/user, Thèmes, Filter, Docker'],
    ['Démarrage rapide', 'docker compose up -d, ant deploy, localhost:8080/gesusers2'],
    ['Identifiants test', 'jdupont / password123 (admin) · mmartin / password456 (user)'],
    ['Architecture', 'Diagramme 3 tiers ou description MVC + DAO + Service + Filter'],
]
readme_table = Table(readme_data, colWidths=[(W-40*mm)*0.3, (W-40*mm)*0.7])
readme_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), HexColor('#1a1a2e')),
    ('TEXTCOLOR', (0,0), (-1,0), white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [white, GRAY_L]),
    ('TOPPADDING', (0,0), (-1,-1), 7),
    ('BOTTOMPADDING', (0,0), (-1,-1), 7),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
    ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ('GRID', (0,0), (-1,-1), 0.5, GRAY_B),
    ('ROUNDEDCORNERS', [4,4,4,4]),
]))
story.append(readme_table)
story.append(sp(10))

story.append(Paragraph('Commande — Ajouter screenshot dans le README', ST['h3']))
story.append(code_block([
    '<font color="#6272a4"># Dans README.md — section Screenshots</font>',
    '<font color="#50fa7b">## Screenshots</font>',
    '',
    '<font color="#f1fa8c">### Mode Clair</font>',
    '![Liste des utilisateurs](docs/screenshot-light.png)',
    '',
    '<font color="#f1fa8c">### Mode Sombre</font>',
    '![Mode sombre](docs/screenshot-dark.png)',
]))
story.append(sp(12))

story.append(Paragraph('Check-list Finale avant Présentation', ST['h2']))
final_checks = [
    ('BDD', 'docker compose up -d  →  MySQL accessible sur 3306, Adminer sur 8081', SUCCESS),
    ('App', 'ant deploy  →  Tomcat démarre gesusers2.war, accès sur localhost:8080', SUCCESS),
    ('SQL', 'Exécuter init.sql si nouvelle BDD  →  table avec colonne role', WARNING),
    ('Test admin', 'Login jdupont/password123  →  sidebar "ADMIN", CRUD complet visible', PRIMARY),
    ('Test user', 'Login mmartin/password456  →  sidebar "USER", boutons masqués', PRIMARY),
    ('Thème', 'Toggle light/dark fonctionne, icône change (☀️ / 🌙)', TEAL),
    ('Redirect', 'Taper /login en étant connecté  →  redirigé vers /list', HexColor('#7c3aed')),
    ('GitHub', 'Repo public avec README à jour + screenshot + commits propres', HexColor('#d97706')),
]
for category, text, color in final_checks:
    # Light version of the color for background
    r, g, b = color.red, color.green, color.blue
    light_bg = colors.Color(r*0.15 + 0.85, g*0.15 + 0.85, b*0.15 + 0.85)
    row_data = [
        Paragraph(f'<b>{category}</b>', ParagraphStyle('fc', fontSize=8, leading=11,
            textColor=color, fontName='Helvetica-Bold', alignment=TA_CENTER)),
        Paragraph(f'☐  {text}', ParagraphStyle('ft', fontSize=9, leading=13,
            textColor=DARK, fontName='Helvetica')),
    ]
    row = Table([row_data], colWidths=[18*mm, (W-40*mm)-20*mm])
    row.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), light_bg),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.4, GRAY_B),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(row)
    story.append(sp(2))

story.append(sp(16))
story.append(hr(PRIMARY, 1.5))
story.append(sp(8))
story.append(Paragraph(
    'Bonne présentation !  —  GesUsers2 · Java EE · Salif Biaye · 2025',
    ParagraphStyle('final', fontSize=11, leading=16, textColor=PRIMARY,
                   fontName='Helvetica-Bold', alignment=TA_CENTER)))

# ── Build ─────────────────────────────────────────────────
doc.build(story, onFirstPage=on_first_page, onLaterPages=on_page)
print(f'PDF généré : {OUTPUT}')
