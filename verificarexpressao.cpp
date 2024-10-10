#include <Arduino.h>
#include <Servo.h>

#define SERVO 6 // Definindo o pino do servo motor

Servo s; // Variável para o servo motor
int pos_atu = 0; // Posição atual do servo

void distribuir_negacao(char expressao[]) {
    char novaExpressao[256];
    int i, j = 0;
    int tam = strlen(expressao);

    for (i = 0; i < tam; i++) {
        if (expressao[i] == '!' && expressao[i + 1] == '(') {
            i += 2; // Pula '!' e '('
            novaExpressao[j++] = '(';
            while (expressao[i] != ')' && expressao[i] != '\0') {
                if (expressao[i] == '&') {
                    novaExpressao[j++] = '|';
                } else if (expressao[i] == '|') {
                    novaExpressao[j++] = '&';
                } else if (expressao[i] == 'P' || expressao[i] == 'Q' || expressao[i] == 'R') {
                    novaExpressao[j++] = '!';
                    novaExpressao[j++] = expressao[i];
                } else {
                    novaExpressao[j++] = expressao[i];
                }
                i++;
            }
            novaExpressao[j++] = ')';
        } else {
            novaExpressao[j++] = expressao[i];
        }
    }
    novaExpressao[j] = '\0';
    strcpy(expressao, novaExpressao);
}

int analisar(const char expressao[], bool p, bool q, bool r) {
    int i, resultado = 0;
    int tam = strlen(expressao);

    for (i = 0; i < tam; i++) {
        char caracter = expressao[i];

        if (caracter == '1')
            resultado = 1;
        else if (caracter == '0')
            resultado = 0;
        else if (caracter == 'P')
            resultado = p;
        else if (caracter == 'Q')
            resultado = q;
        else if (caracter == 'R')
            resultado = r;

        else if (caracter == '!') {
            i++;
            if (expressao[i] == 'P')
                resultado = !p;
            else if (expressao[i] == 'Q')
                resultado = !q;
            else if (expressao[i] == 'R')
                resultado = !r;
            else if (expressao[i] == '1')
                resultado = 0;
            else if (expressao[i] == '0')
                resultado = 1;
        }

        else if (caracter == '&') {
            resultado = resultado && analisar(expressao + i + 1, p, q, r);
            break;
        } else if (caracter == '|') {
            resultado = resultado || analisar(expressao + i + 1, p, q, r);
            break;
        } else if (caracter == '>') {
            resultado = (!resultado) || analisar(expressao + i + 1, p, q, r);
            break;
        } else if (caracter == '(') {
            int j = i + 1;
            int contParenteses = 1;
            while (j < tam && contParenteses > 0) {
                if (expressao[j] == '(') contParenteses++;
                if (expressao[j] == ')') contParenteses--;
                j++;
            }
            char subexpressao[256];
            strncpy(subexpressao, expressao + i + 1, j - i - 2);
            subexpressao[j - i - 2] = '\0';
            resultado = analisar(subexpressao, p, q, r);
            i = j - 1;
        }
    }
    return resultado;
}

void pos_servo(int pos_des) {
    int sid = pos_des - pos_atu;
    if (sid > 0) {
        for (pos_atu = pos_atu; pos_atu < pos_des; pos_atu++) {
            s.write(pos_atu);
            delay(10);
        }
    }
    if (sid < 0) {
        for (pos_atu = pos_atu; pos_atu > pos_des; pos_atu--) {
            s.write(pos_atu);
            delay(10);
        }
    }
}

void avaliar_sentenca(char sentenca[]) {
    distribuir_negacao(sentenca);

    // Resetando os LEDs antes de avaliar a nova sentença
    digitalWrite(2, LOW); // Desliga o LED da contradição
    digitalWrite(3, LOW); // Desliga o LED da satisfatibilidade
    digitalWrite(4, LOW); // Desliga o LED da tautologia

    int i, resultado;
    int cont_true = 0, cont_false = 0;
    bool PTab[8] = {0, 0, 0, 0, 1, 1, 1, 1};
    bool QTab[8] = {0, 0, 1, 1, 0, 0, 1, 1};
    bool RTab[8] = {0, 1, 0, 1, 0, 1, 0, 1};

    Serial.println("\nJustifica -> Tabela Verdade:");
    Serial.print("P\tQ\tR\t");
    Serial.println(sentenca);

    for (i = 0; i < 8; i++) {
        resultado = analisar(sentenca, PTab[i], QTab[i], RTab[i]);

        // Exibe a tabela-verdade
        Serial.print(PTab[i]);
        Serial.print("\t");
        Serial.print(QTab[i]);
        Serial.print("\t");
        Serial.print(RTab[i]);
        Serial.print("\t");
        Serial.println(resultado);

        if (resultado) {
            cont_true++;
        } else {
            cont_false++;
        }
    }

    if (cont_true == 8) {
        Serial.println("\nA sentença é uma Tautologia.");
        digitalWrite(4, HIGH); // LED verde
        pos_servo(125); // Servo motor aponta para o LED verde
        delay(2000); // 2 segundos de delay
    } else if (cont_false == 8) {
        Serial.println("\nA sentença é uma Contradição.");
        digitalWrite(2, HIGH); // LED vermelho
        pos_servo(50); // Servo motor aponta para o LED vermelho
        delay(2000); // 2 segundos de delay
    } else {
        Serial.println("\nA sentença é Satisfatível.");
        digitalWrite(3, HIGH); // LED amarelo
        pos_servo(90); // Servo motor aponta para o LED amarelo
        delay(2000); // 2 segundos de delay
    }
}

void setup() {
    Serial.begin(9600); // Mudança para 9600 baud rate
    pinMode(2, OUTPUT); // LED vermelho (Contradição)
    pinMode(3, OUTPUT); // LED amarelo (Satisfatível)
    pinMode(4, OUTPUT); // LED verde (Tautologia)
    s.attach(SERVO); // Inicia o servo motor
    s.write(0); // Posição inicial do servo em 0 graus
    pos_atu = 0;
    Serial.println("\nColoque apenas 'P', 'Q' ou 'R', além dos operadores lógicos: '&', '!', '>', '|', '(', ')'");
}

void loop() {
    if (Serial.available() > 0) {
        char sentenca[256];
        int len = Serial.readBytesUntil('\n', sentenca, 255);
        sentenca[len] = '\0'; // Certifica que a string tem o terminador correto

        if (strcmp(sentenca, "0") == 0) {
            Serial.println("Programa finalizado.");
            while (true); // Para o loop se o usuário digitar "0"
        }

        avaliar_sentenca(sentenca);
    }
}
