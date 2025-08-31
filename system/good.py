import random
import sys
import time

COLORS = [
    "\033[96m",
    "\033[94m",
    "\033[34m",
    "\033[36m"
    ]
RESET = "\033[0m"

def run(args):
    frases = [
        "Recuerda no perder la cordura, todo va a ir bien ;)",
        "Tu mejor opcion es pensar y hacer el bien siempre!",
        "Todo lo que das, haces y piensas... se te devuelve x2",
        "Podemos ser mejores personas solo con el pensamiento..",
        "Quierete y quiere a los demas! Despues todo se vera mejor incluso si no es asi..",
        "Tus ojos ven mucho mas de lo que piensas y procesas...!",
        "Las drogas/sobre-dopamina y malos habitos son tu peor enemigo ;c ",
        "Eres muy fuerte querid@ usser!< no te rindas nunca>",
        "Las personas pueden ser malas... Pero todo puede mejorar solo con el pensamiento",
        "Podemos escribir en un papel lo que piensas... lo has intentado ?",
        "Es bueno quejarse, sentirse mal, pero nunca te quedes ahi... es solo un punto de partida negativo!",
        "you can always be a good person!",
        "you can always make someone smile!",
        "There are people who love you! (If there aren't any), find that family, even if it's not your blood!",
        "your brothers are your v2",
        "You can debug and see your errors and try to fix them, be your best version!",
        "There are people out there who would want someone like you! Never doubt it!",
        "How about a new version of you? We can try to get out of beta!",
        "The people above see us, but what do we do?",
        "Should we be worried? Yes and no, but never stay at 0.",
        "Do the people above see us the way you see the rest of us?",
        "Do we overclock? Be careful, your heart could become weak!",
        "Does YHWH see us? What if we are really him?",
        "Remember to be a compassionate, calm being",
        "There are many people who appreciate you, don't give up!",
        "Giving up is not in your plans!",
        "You must be strong and never show weakness or fear, it is you!",
        "Always remember to be careful and treat others as you would like to be treated!",
        "Your eyes are so much more than just that, you can be lucky as well as a wretch, the point is to never give up",
        "Learn to think with a cool mind, don't get upset, there you will master everything!",
        "that your good deeds are rewarded multiplied by 3",
        "We love you, don't give up or show weakness, even if you're losing, face it!",
        "Good and bad things will happen but don't worry, life is like that, you just have to learn from the bad and the good and focus on improving the bad and turning it into good!",
        "Why do you limit your mind?",
        "Don't limit yourself, there are things up there that would change everything!",
        "It's okay to go blank, you just need to rest and try again, don't give up!",
        "Remember to sleep, eat, and laugh! Even if you're alone!",
        "Try to reset your brain when you can't take it anymore! Don't act without thinking",
        "Good and evil are normal, just control them! Don't give up!",
        "You will find many loved ones, and when you are there, take good care of them, don't let them down!",
        "अच्छे इंसान बनो, ऊपर वाला तुमसे प्यार करता है",
        "हम सब सुधार कर सकते हैं! बस आपको इस पर विश्वास करना होगा।",
        "कल आप v0-2 थे, आज आप v1 हो सकते हैं",
        "शांति से सोचो, सब कुछ बेहतर हो जाएगा!",
        "निराश मत होइए, हम सभी ऐसे क्षणों से गुजरते हैं!",
        "आपको जारी रखना चाहिए, विचलित न हों!",
        "आपको जिज्ञासु होना चाहिए, लेकिन हमेशा सावधान रहना चाहिए, सचेत रहें, लेकिन कायर नहीं",
        "दूसरों के प्रति सहानुभूति रखें, ठीक वैसे ही जैसे आप चाहते हैं कि वे आपके प्रति रखें",
        "आप जो कुछ भी करते हैं वह आपके पास वापस आता है, इसे मत भूलिए!",
        "एक अच्छे काम में कोई खर्च नहीं होता, है ना?",
        "आप हमेशा अपने अस्तित्व को सुधार सकते हैं और उसमें सुधार ला सकते हैं! खुद को भ्रष्ट मत कीजिए।",
        "बैकअप याद रखें, वे महत्वपूर्ण हैं! मैं सॉफ़्टवेयर की बात नहीं कर रहा हूँ।",
        "प्रेम अच्छा है, लेकिन आत्म-प्रेम उससे भी अधिक अच्छा है, है न?",
        "हमें दुःख के क्षणों में भी खुश रहना चाहिए",
        "अच्छे काम करने के लिए पैसे की जरूरत नहीं होती!",
        "हम सभी में खामियां होती हैं, केवल यह मायने रखता है कि हम उन्हें कैसे स्वीकार करते हैं और उनसे कैसे निपटते हैं।",
        "कोई भी आपको कुछ भी करने के लिए मजबूर नहीं कर सकता, अपनी स्वतंत्र इच्छा का पालन करें लेकिन इसे भ्रमित न करें!",
        "अपने आप पर दबाव मत डालो, अपने रास्ते में आने वाली हर चीज़",
        "खुश रहो"
    ]
    frase =  random.choice(frases)
    color = random.choice(COLORS)
    for letra in frase:
        sys.stdout.write(color + letra + RESET)
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")
