import streamlit as st
import os
from dotenv import load_dotenv

# Configuration de la page
st.set_page_config(
    page_title="Western Ethics Bot",
    page_icon="🏛️",
    layout="wide"
)

# Système de traduction pour l'interface
def get_ui_text(key, language):
    """Textes de l'interface dans toutes les langues"""
    texts = {
        'français': {
            'question_placeholder': "Tapez votre question éthique ici...",
            'question_error': "❌ Veuillez entrer une question",
            'ethics_error': "❌ Cette question ne semble pas porter sur l'éthique ou la philosophie morale",
            'limit_error': "⚠️ Limite de questions gratuites atteinte. Ajoutez votre clé API pour continuer.",
            'responses_header': "📜 Réponses Philosophiques",
            'question_label': "Question:",
            'consulting': "Consultation des philosophes...",
            'analysis': "Analyse philosophique en cours...",
            'synthesis_header': "🎯 Synthèse Philosophique",
            'synthesis_error': "❌ Impossible de générer une synthèse",
            'sources_button': "📚 Voir les sources utilisées",
            'sources_header': "📖 Sources et Extraits",
            'sources_info': "Extraits des œuvres originales utilisés pour générer les réponses",
            'no_content': "❌ Aucun contenu trouvé pour",
            'overload': "⏳ Serveurs surchargés. Réessayez dans une minute.",
            'error_prefix': "❌ Erreur:",
            'your_question': "Votre question:",
            'examples_header': "💡 Exemples de questions",
            'api_key_label': "Votre clé Anthropic (optionnel):",
            'api_key_help': "Pour usage illimité",
            'api_active': "✅ Clé utilisateur active - Usage illimité",
            'free_remaining': "questions gratuites restantes",
            'limit_reached': "⚠️ Limite atteinte. Ajoutez votre clé API.",
            'philosophers_available': "📚 Philosophes Disponibles",
            'button_ask': "🎯 Poser la Question"
        },
        'english': {
            'question_placeholder': "Type your ethical question here...",
            'question_error': "❌ Please enter a question",
            'ethics_error': "❌ This question does not seem to be about ethics or moral philosophy",
            'limit_error': "⚠️ Free question limit reached. Add your API key to continue.",
            'responses_header': "📜 Philosophical Responses",
            'question_label': "Question:",
            'consulting': "Consulting philosophers...",
            'analysis': "Philosophical analysis in progress...",
            'synthesis_header': "🎯 Philosophical Synthesis",
            'synthesis_error': "❌ Unable to generate synthesis",
            'sources_button': "📚 View sources used",
            'sources_header': "📖 Sources and Excerpts",
            'sources_info': "Excerpts from original works used to generate responses",
            'no_content': "❌ No content found for",
            'overload': "⏳ Servers overloaded. Try again in a minute.",
            'error_prefix': "❌ Error:",
            'your_question': "Your question:",
            'examples_header': "💡 Question examples",
            'api_key_label': "Your Anthropic key (optional):",
            'api_key_help': "For unlimited usage",
            'api_active': "✅ User key active - Unlimited usage",
            'free_remaining': "free questions remaining",
            'limit_reached': "⚠️ Limit reached. Add your API key.",
            'philosophers_available': "📚 Available Philosophers",
            'button_ask': "🎯 Ask Question"
        },
        'español': {
            'question_placeholder': "Escriba su pregunta ética aquí...",
            'question_error': "❌ Por favor ingrese una pregunta",
            'ethics_error': "❌ Esta pregunta no parece tratar sobre ética o filosofía moral",
            'limit_error': "⚠️ Límite de preguntas gratuitas alcanzado. Agregue su clave API para continuar.",
            'responses_header': "📜 Respuestas Filosóficas",
            'question_label': "Pregunta:",
            'consulting': "Consultando filósofos...",
            'analysis': "Análisis filosófico en progreso...",
            'synthesis_header': "🎯 Síntesis Filosófica",
            'synthesis_error': "❌ No se pudo generar la síntesis",
            'sources_button': "📚 Ver fuentes utilizadas",
            'sources_header': "📖 Fuentes y Extractos",
            'sources_info': "Extractos de obras originales utilizados para generar respuestas",
            'no_content': "❌ No se encontró contenido para",
            'overload': "⏳ Servidores sobrecargados. Inténtelo de nuevo en un minuto.",
            'error_prefix': "❌ Error:",
            'your_question': "Su pregunta:",
            'examples_header': "💡 Ejemplos de preguntas",
            'api_key_label': "Su clave Anthropic (opcional):",
            'api_key_help': "Para uso ilimitado",
            'api_active': "✅ Clave de usuario activa - Uso ilimitado",
            'free_remaining': "preguntas gratuitas restantes",
            'limit_reached': "⚠️ Límite alcanzado. Agregue su clave API.",
            'philosophers_available': "📚 Filósofos Disponibles",
            'button_ask': "🎯 Hacer Pregunta"
        },
        'deutsch': {
            'question_placeholder': "Geben Sie hier Ihre ethische Frage ein...",
            'question_error': "❌ Bitte geben Sie eine Frage ein",
            'ethics_error': "❌ Diese Frage scheint nicht über Ethik oder Moralphilosophie zu handeln",
            'limit_error': "⚠️ Limit für kostenlose Fragen erreicht. Fügen Sie Ihren API-Schlüssel hinzu, um fortzufahren.",
            'responses_header': "📜 Philosophische Antworten",
            'question_label': "Frage:",
            'consulting': "Philosophen werden konsultiert...",
            'analysis': "Philosophische Analyse läuft...",
            'synthesis_header': "🎯 Philosophische Synthese",
            'synthesis_error': "❌ Synthese konnte nicht erstellt werden",
            'sources_button': "📚 Verwendete Quellen anzeigen",
            'sources_header': "📖 Quellen und Auszüge",
            'sources_info': "Auszüge aus Originalwerken zur Generierung der Antworten",
            'no_content': "❌ Kein Inhalt gefunden für",
            'overload': "⏳ Server überlastet. Versuchen Sie es in einer Minute erneut.",
            'error_prefix': "❌ Fehler:",
            'your_question': "Ihre Frage:",
            'examples_header': "💡 Fragebeispiele",
            'api_key_label': "Ihr Anthropic-Schlüssel (optional):",
            'api_key_help': "Für unbegrenzte Nutzung",
            'api_active': "✅ Benutzerschlüssel aktiv - Unbegrenzte Nutzung",
            'free_remaining': "kostenlose Fragen verbleibend",
            'limit_reached': "⚠️ Limit erreicht. Fügen Sie Ihren API-Schlüssel hinzu.",
            'philosophers_available': "📚 Verfügbare Philosophen",
            'button_ask': "🎯 Frage Stellen"
        }
    }
    return texts.get(language, texts['english']).get(key, key)

# Chargement du système RAG
@st.cache_resource
def load_rag_system():
    try:
        from mywesternethicsbot_rag import BulletproofRAGSystem
        import anthropic
        
        # Protection pour la clé API
        load_dotenv()
        bot_api_key = os.getenv('ANTHROPIC_API_KEY')
        
        if not bot_api_key:
            return None, None
            
        # Initialiser le système RAG
        system = BulletproofRAGSystem(anthropic_api_key=bot_api_key)
        collection = system.get_collection_safely("western_ethics_safe")
        
        return system, collection
        
    except Exception as e:
        # Capture TOUTES les erreurs (clé API, ChromaDB, etc.)
        st.error(f"❌ Mode dégradé : {e}")
        return None, None

# Initialisation du système
system, collection = load_rag_system()

# Vérifier si le système est chargé
if system is None or collection is None:
    st.error("❌ Impossible de charger le système RAG")
    st.stop()

# Détection des philosophes disponibles
@st.cache_data
def get_available_philosophers():
    """Détecte les philosophes disponibles"""
    try:
        sample = collection.get(limit=6000, include=["metadatas"])  # ÉCHANTILLON MASSIF !
        authors = set()
        for meta in sample["metadatas"]:
            author = meta.get("author", "Unknown")
            if author != "Unknown":
                authors.add(author)
        return sorted(list(authors))
    except:
        return ["Platon", "Kant", "Rawls", "Augustine", "Spinoza", "Bentham"]

available_philosophers = get_available_philosophers()

# Header principal
st.title("🏛️ Western Ethics Bot")
st.markdown("*Où l'IA rencontre la sagesse éternelle*")

# Sidebar pour configuration
with st.sidebar:
    st.header("🌍 Configuration")
    
    # Sélection de langue élégante
    st.subheader("Langue / Language")
    
    language_options = {
        "🇫🇷 Français": "français",
        "🇺🇸 English": "english", 
        "🇪🇸 Español": "español",
        "🇩🇪 Deutsch": "deutsch"
    }
    
    selected_language = st.selectbox(
        "Choisissez votre langue:",
        list(language_options.keys()),
        index=0
    )
    current_language = language_options[selected_language]
    
    # Mode de réponse
    st.subheader("Mode de Réponse")
    mode_options = {
        "français": ["🎭 Réponses individuelles", "🎯 Synthèse philosophique"],
        "english": ["🎭 Individual responses", "🎯 Philosophical synthesis"],
        "español": ["🎭 Respuestas individuales", "🎯 Síntesis filosófica"],
        "deutsch": ["🎭 Individuelle Antworten", "🎯 Philosophische Synthese"]
    }
    
    mode = st.radio(
        "Sélectionnez le mode:",
        mode_options.get(current_language, mode_options["english"])
    )
    
    # Gestion clé API utilisateur
    st.subheader("🔑 Clé API")
    user_api_key = st.text_input(
        get_ui_text('api_key_label', current_language),
        type="password",
        help=get_ui_text('api_key_help', current_language)
    )
    
    if user_api_key:
        st.success(get_ui_text('api_active', current_language))
    else:
        # Gestion des questions gratuites
        if 'free_questions_used' not in st.session_state:
            st.session_state.free_questions_used = 0
        
        remaining = 3 - st.session_state.free_questions_used
        if remaining > 0:
            st.info(f"🎁 {remaining} {get_ui_text('free_remaining', current_language)}")
        else:
            st.warning(get_ui_text('limit_reached', current_language))
    
    # Info philosophes avec style
    st.subheader(get_ui_text('philosophers_available', current_language))
    
    # Affichage en colonnes des philosophes
    for i in range(0, len(available_philosophers), 2):
        cols = st.columns(2)
        with cols[0]:
            if i < len(available_philosophers):
                st.write(f"🎭 {available_philosophers[i]}")
        with cols[1]:
            if i + 1 < len(available_philosophers):
                st.write(f"🎭 {available_philosophers[i + 1]}")

# Zone principale avec mise en page élégante
st.header("💭 Posez votre question philosophique")

# Exemples de questions multilingues avec style
examples = {
    "français": [
        "• Qu'est-ce que la justice ?",
        "• Comment devrions-nous vivre éthiquement ?",
        "• Quelle est la nature du bien et du mal ?",
        "• Qu'est-ce qui rend une action morale ?"
    ],
    "english": [
        "• What is justice?",
        "• How should we live ethically?", 
        "• What is the nature of good and evil?",
        "• What makes an action moral?"
    ],
    "español": [
        "• ¿Qué es la justicia?",
        "• ¿Cómo deberíamos vivir éticamente?",
        "• ¿Cuál es la naturaleza del bien y del mal?",
        "• ¿Qué hace que una acción sea moral?"
    ],
    "deutsch": [
        "• Was ist Gerechtigkeit?",
        "• Wie sollten wir ethisch leben?",
        "• Was ist die Natur von Gut und Böse?",
        "• Was macht eine Handlung moralisch?"
    ]
}

with st.expander(get_ui_text('examples_header', current_language)):
    # Affichage des exemples en colonnes
    col1, col2 = st.columns(2)
    current_examples = examples.get(current_language, examples["english"])
    
    with col1:
        for example in current_examples[:2]:
            st.write(example)
    
    with col2:
        for example in current_examples[2:]:
            st.write(example)

# Zone de question élégante
question = st.text_area(
    get_ui_text('your_question', current_language),
    height=100,
    placeholder=get_ui_text('question_placeholder', current_language)
)

# Fonction pour vérifier si question éthique
def is_ethics_related(question, api_key):
    """Vérification simple si la question porte sur l'éthique"""
    if not question:
        return False
    
    ethics_keywords = [
        'éthique', 'moral', 'justice', 'vertu', 'bien', 'mal', 'devoir',
        'ethics', 'moral', 'justice', 'virtue', 'good', 'evil', 'duty',
        'ética', 'moral', 'justicia', 'virtud', 'recht', 'ethik'
    ]
    
    question_lower = question.lower()
    return any(keyword in question_lower for keyword in ethics_keywords)

# Fonction pour créer les prompts sophistiqués (anti-banalité)
def create_sophisticated_prompt(author, question, context, language):
    """Crée des prompts sophistiqués avec instructions anti-banalité"""
    
    if language == 'français':
        return f"""En tant que {author}, vous allez répondre à cette question avec la profondeur qui vous caractérise.

MATÉRIAUX DE RÉFLEXION:
{context}

QUESTION: {question}

INSTRUCTIONS STRICTES:
• Répondez en français dans le style d'un professeur de philosophie aimant partager
• Intégrez naturellement les idées comme si c'était votre propre réflexion
• NE MENTIONNEZ JAMAIS "les passages", "le texte dit" ou "selon le passage"
• Si les informations ne suffisent pas, dites-le avec finesse
• Développez votre pensée avec des exemples et des nuances
• Adoptez un ton académique mais accessible, ni télégraphique ni pompeux
• Montrez la richesse de votre réflexion philosophique
• ÉVITEZ absolument les phrases génériques comme "il est important de", "on peut dire que"

Votre réflexion philosophique en tant que {author}:"""

    elif language == 'english':
        return f"""As {author}, you will answer this question with the depth that characterizes your thought.

MATERIALS FOR REFLECTION:
{context}

QUESTION: {question}

STRICT INSTRUCTIONS:
• Answer in English in the style of a philosophy professor who loves to share
• Integrate ideas naturally as if they were your own reflection
• NEVER mention "the passages", "the text says" or "according to the passage"
• If the information is insufficient, say so clearly but with finesse
• Develop your thought with examples and nuances
• Adopt a professorial but accessible tone, neither telegraphic nor pompous
• Show the richness of your philosophical reflection
• ABSOLUTELY AVOID generic phrases like "it is important to", "one can say that"

Your philosophical reflection as {author}:"""

    elif language == 'español':
        return f"""Como {author}, responderá a esta pregunta con la profundidad que caracteriza su pensamiento.

MATERIALES PARA LA REFLEXIÓN:
{context}

PREGUNTA: {question}

INSTRUCCIONES ESTRICTAS:
• Responda en español al estilo de un profesor de filosofía que ama compartir
• Integre las ideas naturalmente como si fueran su propia reflexión
• NUNCA mencione "los pasajes", "el texto dice" o "según el pasaje"
• Si la información no es suficiente, dígalo claramente pero con delicadeza
• Desarrolle su pensamiento con ejemplos y matices
• Adopte un tono profesoral pero accesible, ni telegráfico ni pomposo
• Muestre la riqueza de su reflexión filosófica
• EVITE absolutamente frases genéricas como "es importante", "se puede decir que"

Su reflexión filosófica como {author}:"""

    else:  # deutsch
        return f"""Als {author}, werden Sie diese Frage mit der Tiefe beantworten, die Ihr Denken charakterisiert.

MATERIALIEN FÜR DIE REFLEXION:
{context}

FRAGE: {question}

STRENGE ANWEISUNGEN:
• Antworten Sie auf Deutsch im Stil eines Philosophieprofessors der gerne teilt
• Integrieren Sie Ideen natürlich, als wären sie Ihre eigene Reflexion
• Erwähnen Sie NIEMALS "die Passagen", "der Text sagt" oder "laut Passage"
• Wenn die Informationen nicht ausreichen, sagen Sie es klar aber mit Feingefühl
• Entwickeln Sie Ihren Gedanken mit Beispielen und Nuancen
• Nehmen Sie einen professoralen aber zugänglichen Ton an, weder telegrafisch noch pompös
• Zeigen Sie den Reichtum Ihrer philosophischen Reflexion
• Vermeiden Sie unbedingt generische Phrasen wie "es ist wichtig", "man kann sagen"

Ihre philosophische Reflexion als {author}:"""

# Fonction pour interroger un philosophe
def ask_philosopher(philosopher, question, api_key, language):
    """Interroge un philosophe spécifique avec prompts sophistiqués"""
    try:
        import anthropic
        
        # Utiliser la clé utilisateur ou celle du bot
        client = anthropic.Anthropic(api_key=api_key)
        
        # Recherche dans les sources
        search_results = system.search_by_author(collection, philosopher, question, n_results=3)
        
        if not search_results or not search_results['documents'][0]:
            return f"{get_ui_text('no_content', language)} {philosopher}", []
        
        # Construire le contexte
        relevant_passages = search_results['documents'][0]
        context = "\n\n".join([f"Passage {i+1}: {passage}" 
                              for i, passage in enumerate(relevant_passages)])
        
        # Utiliser le prompt sophistiqué
        prompt = create_sophisticated_prompt(philosopher, question, context, language)
        
        # System prompts par langue
        system_prompts = {
            'français': f"Vous êtes {philosopher}, un philosophe de référence. Répondez ENTIÈREMENT en français dans un style professoral accessible mais profond. Basez-vous uniquement sur les passages fournis.",
            'english': f"You are {philosopher}, a great philosopher. Respond ENTIRELY in English in an accessible but profound professorial style. Base your response only on the passages provided.",
            'español': f"Usted es {philosopher}, un gran filósofo. Responda COMPLETAMENTE en español con un estilo profesoral accesible pero profundo. Base su respuesta únicamente en los pasajes proporcionados.",
            'deutsch': f"Sie sind {philosopher}, ein großer Philosoph. Antworten Sie VOLLSTÄNDIG auf Deutsch in einem zugänglichen aber tiefen professoralen Stil. Stützen Sie Ihre Antwort nur auf die bereitgestellten Passagen."
        }
        
        # Génération de la réponse
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            system=system_prompts.get(language, system_prompts['english']),
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.content[0].text, search_results['metadatas'][0]
        
    except Exception as e:
        error_str = str(e)
        if "529" in error_str or "overloaded" in error_str.lower():
            return get_ui_text('overload', language), []
        else:
            return f"{get_ui_text('error_prefix', language)} {str(e)}", []

# Fonction pour créer une synthèse sophistiquée
def create_synthesis(question, responses, api_key, language):
    """Crée une synthèse sophistiquée anti-banalité"""
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)
        
        # Construire le contexte du dialogue
        dialogue_context = f"Question: {question}\n\n"
        for philosopher, response in responses.items():
            dialogue_context += f"{philosopher}: {response}\n\n"
        
        # Prompts anti-banalité par langue
        if language == 'français':
            prompt = f"""Vous êtes un professeur de philosophie de haut niveau. Analysez ces perspectives avec une rigueur académique exceptionnelle.

{dialogue_context}

Créez une synthèse structurée en 3 sections précises:

**CONVERGENCES PHILOSOPHIQUES:**
[Identifiez les points d'accord conceptuels précis, avec arguments]

**DIVERGENCES THÉORIQUES:**
[Analysez les oppositions fondamentales, expliquez pourquoi elles existent]

**APPORT CRITIQUE:**
[Évaluez quelle approche est la plus convaincante et pourquoi]

INSTRUCTIONS STRICTES:
• INTERDICTION absolue de phrases banales comme "cette analyse suggère que...", "une compréhension complète nécessite...", "cette réflexion montre que..."
• Évitez toute conclusion générique ou passe-partout
• Terminez par un jugement philosophique substantiel et précis
• Style académique mais incisif, pas de langue de bois
• Concentrez-vous sur les enjeux philosophiques réels, pas sur des platitudes

Synthèse philosophique rigoureuse:"""

        elif language == 'english':
            prompt = f"""You are a high-level philosophy professor. Analyze these perspectives with exceptional academic rigor.

{dialogue_context}

Create a structured synthesis in 3 precise sections:

**PHILOSOPHICAL CONVERGENCES:**
[Identify precise conceptual agreements, with arguments]

**THEORETICAL DIVERGENCES:**
[Analyze fundamental oppositions, explain why they exist]

**CRITICAL CONTRIBUTION:**
[Evaluate which approach is most convincing and why]

STRICT INSTRUCTIONS:
• ABSOLUTE PROHIBITION of banal phrases like "this analysis suggests that...", "a comprehensive understanding requires...", "this reflection shows that..."
• Avoid any generic or catch-all conclusions
• End with a substantial and precise philosophical judgment
• Academic but incisive style, no empty rhetoric
• Focus on real philosophical issues, not platitudes

Rigorous philosophical synthesis:"""

        elif language == 'español':
            prompt = f"""Usted es un profesor de filosofía de alto nivel. Analice estas perspectivas con rigor académico excepcional.

{dialogue_context}

Cree una síntesis estructurada en 3 secciones precisas:

**CONVERGENCIAS FILOSÓFICAS:**
[Identifique acuerdos conceptuales precisos, con argumentos]

**DIVERGENCIAS TEÓRICAS:**
[Analice las oposiciones fundamentales, explique por qué existen]

**CONTRIBUCIÓN CRÍTICA:**
[Evalúe qué enfoque es más convincente y por qué]

INSTRUCCIONES ESTRICTAS:
• PROHIBICIÓN absoluta de frases banales como "este análisis sugiere que...", "una comprensión completa requiere...", "esta reflexión muestra que..."
• Evite cualquier conclusión genérica o comodín
• Termine con un juicio filosófico sustancial y preciso
• Estilo académico pero incisivo, no retórica vacía
• Concéntrese en cuestiones filosóficas reales, no en tópicos

Síntesis filosófica rigurosa:"""

        else:  # deutsch
            prompt = f"""Sie sind ein hochrangiger Philosophieprofessor. Analysieren Sie diese Perspektiven mit außergewöhnlicher akademischer Strenge.

{dialogue_context}

Erstellen Sie eine strukturierte Synthese in 3 präzisen Abschnitten:

**PHILOSOPHISCHE KONVERGENZEN:**
[Identifizieren Sie präzise konzeptionelle Übereinstimmungen, mit Argumenten]

**THEORETISCHE DIVERGENZEN:**
[Analysieren Sie fundamentale Gegensätze, erklären Sie warum sie existieren]

**KRITISCHER BEITRAG:**
[Bewerten Sie welcher Ansatz überzeugender ist und warum]

STRENGE ANWEISUNGEN:
• ABSOLUTES VERBOT banaler Phrasen wie "diese Analyse deutet darauf hin, dass...", "ein umfassendes Verständnis erfordert...", "diese Reflexion zeigt, dass..."
• Vermeiden Sie jede generische oder Allzweck-Schlussfolgerung
• Beenden Sie mit einem substantiellen und präzisen philosophischen Urteil
• Akademischer aber scharfsinniger Stil, keine leere Rhetorik
• Konzentrieren Sie sich auf echte philosophische Fragen, nicht auf Gemeinplätze

Rigorose philosophische Synthese:"""
        
        # System prompts sophistiqués par langue
        system_prompts = {
            'français': "Vous êtes un professeur de philosophie distingué. Fournissez une analyse académique incisive. Évitez absolument les conclusions génériques et les clichés philosophiques. Répondez entièrement en français.",
            'english': "You are a distinguished philosophy professor. Provide incisive academic analysis. Absolutely avoid generic conclusions and philosophical clichés. Respond entirely in English.",
            'español': "Usted es un distinguido profesor de filosofía. Proporcione un análisis académico incisivo. Evite absolutamente las conclusiones genéricas y los clichés filosóficos. Responda completamente en español.",
            'deutsch': "Sie sind ein angesehener Philosophieprofessor. Liefern Sie eine scharfsinnige akademische Analyse. Vermeiden Sie unbedingt generische Schlussfolgerungen und philosophische Klischees. Antworten Sie vollständig auf Deutsch."
        }
        
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            system=system_prompts.get(language, system_prompts['english']),
            max_tokens=1200,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.content[0].text
        
    except Exception as e:
        error_str = str(e)
        if "529" in error_str or "overloaded" in error_str.lower():
            return get_ui_text('overload', language)
        else:
            return f"{get_ui_text('error_prefix', language)} {str(e)}"

# Bouton de soumission centré et élégant
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    ask_button = st.button(
        get_ui_text('button_ask', current_language),
        type="primary",
        use_container_width=True
    )

if ask_button:
    if not question.strip():
        st.error(get_ui_text('question_error', current_language))
    elif not is_ethics_related(question, user_api_key):
        st.error(get_ui_text('ethics_error', current_language))
    else:
        # Vérifier les limites
        if not user_api_key and st.session_state.free_questions_used >= 3:
            st.error(get_ui_text('limit_error', current_language))
        else:
            # Utiliser la clé utilisateur ou celle du bot
            api_key_to_use = user_api_key if user_api_key else os.getenv('ANTHROPIC_API_KEY')
            
            # Incrémenter le compteur si utilisation gratuite
            if not user_api_key:
                st.session_state.free_questions_used += 1
            
            # Affichage élégant de la question
            st.markdown("---")
            st.subheader(get_ui_text('responses_header', current_language))
            
            # Question dans un container élégant
            with st.container():
                st.markdown(f"**{get_ui_text('question_label', current_language)}** *{question}*")
            
            st.markdown("---")
            
            # Déterminer le mode (gérer les différentes langues)
            is_individual_mode = ("individuel" in mode.lower() or 
                                "individual" in mode.lower() or 
                                "individuales" in mode.lower() or
                                "individuelle" in mode.lower())
            
            if is_individual_mode:
                # Mode individuel avec mise en page en colonnes
                responses = {}
                
                with st.spinner(get_ui_text('consulting', current_language)):
                    # Créer des colonnes pour l'affichage
                    if len(available_philosophers) >= 4:
                        # Affichage sur 2 colonnes si 4+ philosophes
                        col1, col2 = st.columns(2)
                        
                        for i, philosopher in enumerate(available_philosophers):
                            # Alterner entre colonnes
                            current_col = col1 if i % 2 == 0 else col2
                            
                            with current_col:
                                with st.expander(f"🎭 {philosopher}", expanded=True):
                                    answer, sources = ask_philosopher(
                                        philosopher, question, api_key_to_use, current_language
                                    )
                                    st.write(answer)
                                    if answer and not answer.startswith("❌") and not answer.startswith("⏳"):
                                        responses[philosopher] = answer
                    else:
                        # Affichage simple si moins de 4 philosophes
                        for philosopher in available_philosophers:
                            with st.expander(f"🎭 {philosopher}", expanded=True):
                                answer, sources = ask_philosopher(
                                    philosopher, question, api_key_to_use, current_language
                                )
                                st.write(answer)
                                if answer and not answer.startswith("❌") and not answer.startswith("⏳"):
                                    responses[philosopher] = answer
                
                # Option citations avec style
                if responses:
                    st.markdown("---")
                    col1, col2, col3 = st.columns([1, 2, 1])
                    with col2:
                        if st.button(get_ui_text('sources_button', current_language), use_container_width=True):
                            st.subheader(get_ui_text('sources_header', current_language))
                            st.info(get_ui_text('sources_info', current_language))
                            
                            # Afficher les sources de manière élégante
                            for philosopher in responses.keys():
                                with st.expander(f"📖 Sources pour {philosopher}"):
                                    st.write(f"Sources consultées pour la réponse de {philosopher}")
                    
            else:
                # Mode synthèse
                with st.spinner(get_ui_text('analysis', current_language)):
                    # Collecter les réponses
                    responses = {}
                    
                    # Barre de progression pour le mode synthèse
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    for i, philosopher in enumerate(available_philosophers):
                        status_text.text(f"Consultation de {philosopher}...")
                        progress_bar.progress((i + 1) / len(available_philosophers))
                        
                        answer, _ = ask_philosopher(
                            philosopher, question, api_key_to_use, current_language
                        )
                        if answer and not answer.startswith("❌") and not answer.startswith("⏳"):
                            responses[philosopher] = answer
                    
                    # Nettoyer la barre de progression
                    progress_bar.empty()
                    status_text.empty()
                    
                    if responses:
                        # Créer la synthèse sophistiquée
                        synthesis = create_synthesis(
                            question, responses, api_key_to_use, current_language
                        )
                        
                        # Affichage élégant de la synthèse
                        with st.container():
                            st.subheader(get_ui_text('synthesis_header', current_language))
                            
                            # Synthèse dans un container avec style
                            with st.container():
                                st.markdown(synthesis)
                            
                            # Informations complémentaires
                            st.markdown("---")
                            st.caption(f"Synthèse basée sur {len(responses)} perspectives philosophiques")
                    else:
                        st.error(get_ui_text('synthesis_error', current_language))

# Footer élégant avec statistiques
st.markdown("---")

# Statistiques en colonnes
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**🎭 Philosophes**")
    st.caption(f"{len(available_philosophers)} penseurs disponibles")
    for philosopher in available_philosophers[:3]:  # Limiter l'affichage
        st.write(f"• {philosopher}")
    if len(available_philosophers) > 3:
        st.write(f"• ... et {len(available_philosophers) - 3} autres")

with col2:
    st.markdown("**📚 Base de Connaissances**")
    if collection:
        doc_count = collection.count()
        st.caption(f"{doc_count:,} documents philosophiques")
        st.write("• Textes originaux authentiques")
        st.write("• Recherche vectorielle intelligente")
        st.write("• Analyse contextuelle avancée")

with col3:
    st.markdown("**🔧 Technologie**")
    st.caption("Stack technique avancée")
    st.write("• Streamlit (Interface)")
    st.write("• Claude Sonnet 4 (IA)")
    st.write("• ChromaDB (Vectoriel)")
    st.write("• RAG multilingue")

# Analytics de session avec style
if 'session_analytics' not in st.session_state:
    st.session_state.session_analytics = {
        'questions_asked': 0,
        'languages_used': set(),
        'modes_used': set()
    }

# Mise à jour analytics si question posée
if st.session_state.get('last_question') != question and question and ask_button:
    st.session_state.session_analytics['questions_asked'] += 1
    st.session_state.session_analytics['languages_used'].add(current_language)
    st.session_state.session_analytics['modes_used'].add(mode)
    st.session_state.last_question = question

# Affichage des analytics de session (optionnel)
with st.expander("📊 Statistiques de Session"):
    analytics = st.session_state.session_analytics
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Questions Posées", analytics['questions_asked'])
    
    with col2:
        st.metric("Langues Utilisées", len(analytics['languages_used']))
    
    with col3:
        st.metric("Modes Testés", len(analytics['modes_used']))
    
    if analytics['languages_used']:
        st.write("**Langues:** " + ", ".join(analytics['languages_used']))

# Message de fin élégant
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666;'>
        <p><em>"Une vie sans examen ne vaut pas la peine d'être vécue"</em> - Socrate</p>
        <p>Explorez la sagesse éternelle avec l'intelligence artificielle moderne</p>
    </div>
    """, 
    unsafe_allow_html=True
)
