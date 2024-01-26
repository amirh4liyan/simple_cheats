// Amirhossein Alian
// 1402/11/02
// Project 1

#include <iostream>

using namespace std;

bool isLower(char);
bool isUpper(char);
bool isAlphabet(char);
int strlen(string);
bool haveDot(string);
string strip(string);
bool isMember(string, string[]);
bool isExclusion(string word);

const int lenExclusion = 115;
string exclusion[] = {
	"A", "An", "The", "Am", "Is", "Are", "For", "And", "Nor", "But",
	"Our", "Yet", "So", "As", "If", "From", "For", "About", "But",
	"Or", "And", "On", "At", "In", "Above", "Of", "By", "With",
	"Than", "Around", "Under", "To", "I", "Yot", "He", "She", "It",
	"We", "They", "Me", "You", "Him", "Her", "It", "Us", "Them",
	"Mine", "Yours", "His", "Hers", "Its", "Ours", "Theirs", "Who",
	"Whom", "Which", "That", "Where", "Whose", "This", "That",
	"These", "Those", "Myself", "Yourself", "Himself", "Herself",
	"Itself", "Ourselves", "Themselves", "Can", "Could", "May",
	"Might", "Will", "Would", "Shall", "Should", "Must", "Ought to",
	"Needn't", "Mustn't", "Had better", "Be", "Have", "Do", "Not",
	"Was", "Were", "Very", "Much", "Many", "Too", "Little", "Few",
	"Such", "Other", "Lot", "Lots", "What", "Who", "How", "When",
	"Your", "There", "Then", "Use", "Has", "Each", "Any", "Thus"
	"He", "His", "One", "My"
};


const int SIZE = 250;
string finals[SIZE];
int f_counter = 0;
string block[SIZE];
int b_counter = 0;
string temp[SIZE];
int t_counter = 0;
string capitals[SIZE];
int c_counter = 0;

// Store Words separately
string text[SIZE];

int length = 0;

int main() {
        // Read Input From file (for Test Stage)
        //freopen("input.txt", "r", stdin);

	cout << "[in-str] Enter Text: ";
        string word;
        int i = 0;
        while (cin >> word) {
                // break with null character code "\0"
                if (word == "\\0")
                        break;
                // add word to text array
                text[i] = word;
                i++;
        }

        length = i;
        /* check for first word
         * (it can not be done on next loop because i-1 will be out of range) */
        if (isUpper(text[0][0])) {
                capitals[c_counter++] = text[0];
        }
        for (int i = 1; i < length; i++) {
                char first_letter = text[i][0];
                if (isUpper(first_letter)) {
                        capitals[c_counter++] = text[i];
                        if (haveDot(text[i-1])) {
                                temp[t_counter++] = text[i];
                        } else {
				if (isExclusion(text[i])) {
					block[b_counter++] = temp[i];
				} else {
                                	finals[f_counter++] = text[i];
				}
                        }
                }
        }

	for (int i = 0; i < t_counter; i++) {
		if (!isMember(temp[i], finals)) {
			if (isExclusion(temp[i])) {
				block[b_counter++] = temp[i];
			}
		}
	}

	for (int i = 0; i < c_counter; i++) {
		if (!isMember(capitals[i], block))
			cout << strip(capitals[i]) << endl;
	}

        return 0;
}

bool isLower(char letter)
{
        return (letter >= 97 && letter <= 122);
}

bool isUpper(char letter)
{
        return (letter >= 65 && letter <= 90);
}

bool isAlphabet(char letter)
{
        return (isLower(letter) || isUpper(letter));
}

bool haveDot(string word)
{
        int last_char_index = strlen(word) - 1;
        if (word[last_char_index] == '.')
                return true;
        return false;
}

int strlen(string word) {
        int i = 0;
        while (word[i] != '\0')
                i++;
        return i;
}

string strip(string word)
{
        bool reachedAlpha = false;
        int start = 0, end = -1;
        int i = 0;
        while(word[i] != '\0') {
                if (isAlphabet(word[i]) && (!reachedAlpha)) {
                        start = i;
                        reachedAlpha = true;
                }
                if (isAlphabet(word[i]) && reachedAlpha)
                        end = i;
                i++;
        }
        string stripped;
        for (int i = start; i <= end; i++)
                stripped += word[i];
        return stripped;
}

bool isMember(string word, string list[])
{
        for (int i = 0; i < length; i++)
                if (list[i] == word)
                        return true;
        return false;
}

bool isExclusion(string word)
{
        for (int i = 0; i < lenExclusion; i++)
                if (exclusion[i] == word)
                        return true;
        return false;
}
