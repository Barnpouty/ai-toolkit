"""
Page content for the AI Toolkit storefront.

Everything here is taken from the two source PDFs:
  - Starter Kit:  "50+ AI Tools Every Student & Young Professional Should Know in 2026" (20 pages)
  - Bonus guide:  "AI Toolkit for Students & Young Professionals — 2026 Edition" (30 pages)

Keeping copy in one module means the templates stay about layout, and anyone
editing the product description has a single place to check it against the PDFs.
"""

PRODUCT = {
    "name": "AI Toolkit",
    "edition": "2026",
    "starter_title": "AI Starter Kit 2026",
    "starter_full_title": "50+ AI Tools Every Student & Young Professional Should Know in 2026",
    "starter_pages": 20,
    "bonus_title": "AI Toolkit for Students & Young Professionals",
    "bonus_subtitle": "Free & paid AI tools explained simply — when to use them, how they help, what they cost.",
    "bonus_pages": 30,
    "format": "PDF",
}

# --- Guide one: the Starter Kit -------------------------------------------------

CATEGORIES = [
    {
        "slug": "writing",
        "name": "Writing & content",
        "lede": "Drafting, rewriting and polishing text.",
        "tools": [
            ("ChatGPT", "Writing, brainstorming, CVs, emails and research", "Free / paid"),
            ("Claude", "Long-form writing and document analysis", "Free / paid"),
            ("Gemini", "Research and content generation", "Free / paid"),
            ("Grammarly", "Grammar checking and writing improvement", "Free / paid"),
            ("QuillBot", "Paraphrasing and rewriting", "Free / paid"),
            ("Wordtune", "Sentence rephrasing and clarity", "Free / paid"),
        ],
        "tip": "Start with ChatGPT — the guide recommends it as the tool that handles nearly every writing task.",
    },
    {
        "slug": "research",
        "name": "Study & research",
        "lede": "Finding sources, reading papers and checking claims.",
        "tools": [
            ("Perplexity AI", "Research with real-time citations", ""),
            ("Elicit", "AI-assisted academic literature review", ""),
            ("Consensus", "Evidence-based answers drawn from research papers", ""),
            ("Scite AI", "Citation analysis for scientific papers", ""),
            ("Scholarcy", "Fast summaries of research papers", ""),
            ("Research Rabbit", "Discover connected academic papers", "Free"),
        ],
        "tip": "Perplexity cites its sources, which makes it the guide's pick for fact-checking and academic research.",
    },
    {
        "slug": "design",
        "name": "Design & presentations",
        "lede": "Slides, posters, CVs and visual documents.",
        "tools": [
            ("Canva AI", "Social media, posters, CVs and presentations in one place", ""),
            ("Gamma", "Turn a prompt into a full presentation", ""),
            ("Beautiful.ai", "Clean, professional slide decks", ""),
            ("Tome AI", "Storytelling-style presentations", ""),
            ("Visme", "Infographics, reports and visual content", ""),
            ("Pitch", "Startup pitch decks with collaboration tools", ""),
        ],
        "tip": "Canva AI can build a complete presentation from a single text prompt — no design background needed.",
    },
    {
        "slug": "images",
        "name": "Image generation",
        "lede": "Illustrations and visuals without a camera.",
        "tools": [
            ("Midjourney", "Studio-quality artwork and illustrations", ""),
            ("Leonardo AI", "Versatile creative image generation", "Free tier"),
            ("Adobe Firefly", "Commercially safe images for professional use", ""),
            ("Playground AI", "Marketing and social media visuals", "Free"),
            ("Freepik AI Generator", "Quick images integrated with stock assets", ""),
            ("Ideogram", "Images with accurate, legible text", ""),
        ],
        "tip": "Use Ideogram when an image needs readable text — other generators often distort lettering.",
    },
    {
        "slug": "career",
        "name": "Career & job search",
        "lede": "CVs, applications, tracking and your profile.",
        "tools": [
            ("Kickresume", "CV builder with professional templates", ""),
            ("Resume.io", "Clean, ATS-friendly resume builder", ""),
            ("Teal HQ", "Track every job application in one dashboard", ""),
            ("Jobscan", "Optimise your CV for applicant tracking systems", ""),
            ("Huntr", "Visual board for managing applications", ""),
            ("LinkedIn AI tools", "Profile optimisation and networking help", ""),
        ],
        "tip": "Most of the tools in this category have a free plan.",
    },
    {
        "slug": "productivity",
        "name": "Productivity",
        "lede": "Notes, schedules, tasks and team work.",
        "tools": [
            ("Notion AI", "Notes, wikis and project management with writing assist", ""),
            ("Motion", "Builds and adjusts your daily schedule", ""),
            ("Reclaim AI", "Syncs habits, tasks and meetings across your calendar", ""),
            ("ClickUp AI", "Team project management with summaries and automation", ""),
            ("Taskade AI", "Task lists, mind maps and team workflows", ""),
            ("Trevor AI", "Daily planner that slots tasks into your calendar", ""),
        ],
        "tip": "Reclaim AI and Trevor AI find a time slot for each task automatically.",
    },
    {
        "slug": "video",
        "name": "Video creation",
        "lede": "From script to finished, captioned video.",
        "tools": [
            ("CapCut AI", "Mobile-first editing with auto-captions and effects", "Free"),
            ("Pictory", "Turn blog posts or scripts into videos", ""),
            ("InVideo AI", "Promotional videos from text prompts", ""),
            ("Synthesia", "AI avatar presenter videos without a camera", ""),
            ("Descript", "Edit audio and video by editing the transcript", ""),
            ("VEED AI", "Social video with subtitles and branding", ""),
        ],
        "tip": "CapCut AI is free and adds subtitles in seconds — useful for any social media content.",
    },
    {
        "slug": "coding",
        "name": "Coding & tech",
        "lede": "Writing, understanding and shipping code.",
        "tools": [
            ("GitHub Copilot", "Code suggestions inside your editor", ""),
            ("Cursor AI", "AI-first editor that rewrites and explains code", ""),
            ("Replit AI", "Code, run and deploy apps in the browser", "Free tier"),
            ("Bolt.new", "Build full-stack web apps from a text description", ""),
            ("Codeium", "Free coding assistant for most editors", "Free"),
            ("Tabnine", "Code completion trained on your codebase", ""),
        ],
        "tip": "Bolt.new lets you describe an app in plain English and generates working code.",
    },
]

WORKFLOWS = [
    {
        "title": "Research a topic, step by step",
        "source": "From “How to research anything in under 10 minutes”",
        "steps": [
            "Find cited sources on your topic with Perplexity AI",
            "Drop papers into Scholarcy for summaries",
            "Use Research Rabbit to find related studies and authors",
            "Check Consensus for evidence-backed conclusions",
            "Verify claims with Scite AI’s citation analysis",
        ],
    },
    {
        "title": "Run your job search with AI",
        "source": "From “5 ways AI can boost your job search today”",
        "steps": [
            "Tailor your CV to each job description with ChatGPT",
            "Run the CV through Jobscan to check ATS matching",
            "Track every application in Teal HQ",
            "Ask ChatGPT to simulate interview questions for the role",
            "Design a one-page CV or portfolio with Canva AI",
        ],
    },
    {
        "title": "The 7-day AI challenge",
        "source": "Choose five tools, use them daily for a week, and track:",
        "steps": [
            "Time saved on tasks",
            "Tasks completed faster than before",
            "New skills or workflows learned",
            "Productivity improvements you noticed",
        ],
        "outcome": "By day seven you know which tools earn a place in your routine — and which to drop.",
    },
]

QUICK_STARTS = [
    {
        "role": "Students",
        "summary": "Assignments, research, presentations and proofreading.",
        "tools": ["ChatGPT", "Perplexity AI", "Canva AI", "Grammarly", "Gamma"],
    },
    {
        "role": "Job seekers",
        "summary": "Tailored CVs, a stronger profile and an organised search.",
        "tools": ["ChatGPT", "LinkedIn AI tools", "Teal HQ", "Jobscan", "Canva AI"],
    },
    {
        "role": "Entrepreneurs",
        "summary": "Pitches, brand assets, operations and market research.",
        "tools": ["ChatGPT", "Canva AI", "Notion AI", "Gamma", "Perplexity AI"],
    },
    {
        "role": "Researchers",
        "summary": "Literature reviews, paper summaries and evidence checks.",
        "tools": ["Perplexity AI", "Elicit", "Consensus", "Research Rabbit", "ChatGPT"],
    },
]

# --- Guide two: the bonus -------------------------------------------------------

BONUS_RULE = (
    "Start free. Upgrade only when the free limit costs you more time "
    "or stress than the monthly fee."
)

WHEN_FREE = [
    "You need explanations, outlines or first drafts a few times a week",
    "You work with your own notes and PDFs — NotebookLM is free",
    "You only need basic grammar checks and short paraphrasing",
    "You code occasionally and can use GitHub’s student offer",
]

WHEN_PAID = [
    "You hit daily or hourly limits during exam or project crunch time",
    "You need longer context — big PDFs, long reports, thesis chapters",
    "You want faster answers and the newest models",
    "You need reliable citations for research papers",
    "You use the tool every single workday",
]

# Four of the nine rows are shown on the page; the full table is in the guide.
DECISION_GUIDE = [
    ("Explanation needed now", "ChatGPT, Claude or Gemini free", "Plus / Pro if limits hit"),
    ("Sources for a paper", "Perplexity free", "Education Pro if research is heavy"),
    ("Slides due tomorrow", "Canva free or Gamma free credits", "Canva Pro if frequent"),
    ("Job applications", "Free resume tool + ChatGPT", "Paid resume tool if many applications"),
]
DECISION_GUIDE_TOTAL = 9

STACKS = [
    {
        "name": "Minimal free stack",
        "cost": "Zero cost",
        "items": [
            "One general chatbot — ChatGPT, Claude, Gemini or Grok",
            "NotebookLM for your own documents",
            "Grammarly free or browser spell-check",
            "Canva free for visuals",
            "GitHub Copilot if you code and qualify as a student",
        ],
    },
    {
        "name": "Strong student stack",
        "cost": "Low cost",
        "items": [
            "Perplexity Education Pro if you research a lot",
            "Notion for organisation, often free for students",
            "One paid chatbot, only if free limits block you regularly",
        ],
    },
    {
        "name": "Young professional stack",
        "cost": "Use what work provides",
        "items": [
            "Keep the free core",
            "Microsoft Copilot or Google AI if your workplace provides it",
            "A paid resume or interview tool during active job searches only",
        ],
    },
]

BONUS_CHAPTERS = [
    ("Free vs paid", "When free is enough, when paying makes sense, and student discounts"),
    ("The free stack", "Eight tools that cover most study and early-career work, compared side by side"),
    ("General AI assistants", "ChatGPT, Claude, Google Gemini and Grok — what each is best for"),
    ("Research & study", "NotebookLM, Perplexity, Elicit, Consensus, Semantic Scholar, ResearchRabbit, Wolfram Alpha, Photomath"),
    ("Writing & editing", "Grammarly, QuillBot, DeepL Write — and a word on AI detection"),
    ("Notes & productivity", "Notion, Otter.ai and the AI already built into Microsoft 365 and Google Workspace"),
    ("Coding, design & career", "GitHub Copilot, Cursor, Canva, Gamma, resume builders and interview practice"),
    ("Using AI well", "A quick decision guide, five working rules and how to build your personal stack"),
]

RULES = [
    ("Write clear prompts", "Tell the tool who you are, what you need and any limits."),
    ("Always verify", "AI can invent facts, papers or numbers. Check anything you submit or publish."),
    ("Follow your school or company rules", "Using AI openly and editing heavily is almost always safer than hiding it."),
    ("Use AI to learn, not to skip learning", "Ask for explanations and practice problems, then do the work yourself."),
    ("Protect your privacy and data", "Don’t paste personal, sensitive or confidential information."),
]

CLOSING_QUOTE = (
    "The people who get the most from AI are not the ones who use the most tools. "
    "They are the ones who use a few tools well, on the right tasks, at the right time."
)

# --- Page previews --------------------------------------------------------------

PREVIEWS = [
    ("preview-starter-contents.webp", "Starter Kit", "What’s inside: the eight categories"),
    ("preview-research-workflow.webp", "Starter Kit", "The five-step research workflow"),
    ("preview-7-day-challenge.webp", "Starter Kit", "Your 7-day AI challenge"),
    ("preview-when-free.webp", "Bonus guide", "When free is enough"),
    ("preview-decision-guide.webp", "Bonus guide", "Quick decision guide"),
    ("preview-personal-stack.webp", "Bonus guide", "Building your personal stack"),
]

# --- FAQ ------------------------------------------------------------------------
# Answers only state what the PDFs or the purchase flow can confirm.

FAQ = [
    (
        "What exactly do I get?",
        "Two PDF guides. The AI Starter Kit 2026 (20 pages) maps AI tools across eight categories, "
        "with quick-start plans for students, job seekers, entrepreneurs and researchers, two step-by-step "
        "workflows and a 7-day challenge. The bonus guide, AI Toolkit for Students & Young Professionals "
        "(30 pages), explains free versus paid tools, what each is best for, and how to use AI responsibly.",
    ),
    (
        "Is this a physical book?",
        "No. Both guides are digital PDF files. Nothing is shipped.",
    ),
    (
        "How do I receive the guides after paying?",
        "Payment is handled on an external checkout page run by EscalePay — no card details are entered on this website. After your payment is confirmed, "
        "follow the access instructions shown by the checkout. Keep your payment confirmation in case you need to contact us.",
    ),
    (
        "How much does it cost?",
        "The current price is shown on the checkout page before you pay. You can review it there without any commitment.",
    ),
    (
        "Is it suitable for beginners?",
        "Yes. The bonus guide is written in plain language and says it directly: you don’t need to become an AI expert, "
        "you only need to know which tool fits the job in front of you. The quick-start plans tell you where to begin.",
    ),
    (
        "Will I have to pay for the tools?",
        "Not necessarily. Many of the tools have free plans, and the bonus guide is built around starting free and "
        "upgrading only when a free limit genuinely gets in your way. It also covers student discounts.",
    ),
    (
        "Is this about getting AI to do my work for me?",
        "No. The guides treat AI as an editor and a tutor, not a ghostwriter. They cover AI detection, following your "
        "school or company rules, verifying facts and never inventing experience on a CV.",
    ),
    (
        "Are the tool prices and offers still current?",
        "AI tools change quickly — plans, prices and student offers come and go. The guides describe what each tool is for "
        "and advise you to check current offers on the official websites before you pay for anything.",
    ),
    (
        "Can I read it on my phone?",
        "Yes. PDF files open on phones, tablets and computers. The pages are laid out in a portrait format that reads well on a phone.",
    ),
]
