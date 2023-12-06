# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\67")
        buf.write("\u01e0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\3\2\7\2j\n\2\f\2\16\2m\13\2\3\2\3\2\3\3\3\3\3\3\3\3\5")
        buf.write("\3u\n\3\3\3\3\3\7\3y\n\3\f\3\16\3|\13\3\3\3\3\3\3\4\3")
        buf.write("\4\5\4\u0082\n\4\3\5\3\5\5\5\u0086\n\5\3\6\5\6\u0089\n")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u0095\n")
        buf.write("\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\5\t\u009e\n\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\5\n\u00a5\n\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\5\13\u00b8\n\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\5\16\u00c6\n\16\3\17\3\17\5\17\u00ca\n")
        buf.write("\17\3\20\3\20\3\20\3\20\3\20\5\20\u00d1\n\20\3\20\3\20")
        buf.write("\3\20\3\21\5\21\u00d7\n\21\3\21\3\21\3\21\5\21\u00dc\n")
        buf.write("\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\5\23\u00e9\n\23\3\24\3\24\3\24\3\24\3\25\3\25\5")
        buf.write("\25\u00f1\n\25\3\26\3\26\3\26\3\26\5\26\u00f7\n\26\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\5\30\u0101\n\30\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31")
        buf.write("\u010d\n\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\5\33\u011d\n\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\5\34\u0125\n\34\3\34\5\34\u0128\n")
        buf.write("\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3 \3 \7 \u013a\n \f \16 \u013d\13 \3!\3!")
        buf.write("\3!\3!\3!\3!\7!\u0145\n!\f!\16!\u0148\13!\3\"\3\"\3\"")
        buf.write("\3\"\3\"\5\"\u014f\n\"\3#\3#\3#\3#\3#\5#\u0156\n#\3$\3")
        buf.write("$\3$\3$\3$\3$\7$\u015e\n$\f$\16$\u0161\13$\3%\3%\3%\5")
        buf.write("%\u0166\n%\3&\3&\3&\3&\3&\3&\7&\u016e\n&\f&\16&\u0171")
        buf.write("\13&\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u0179\n\'\3(\3(\3(\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\3(\3(\3(\7(\u0188\n(\f(\16(\u018b")
        buf.write("\13(\3)\3)\3)\3)\3)\3)\3)\5)\u0194\n)\3*\3*\3*\3*\3*\5")
        buf.write("*\u019b\n*\3+\3+\3+\3+\3+\5+\u01a2\n+\3,\3,\3,\5,\u01a7")
        buf.write("\n,\3-\3-\3.\3.\3.\3.\5.\u01af\n.\3/\3/\3/\3/\3/\3/\3")
        buf.write("/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\5/\u01c6\n")
        buf.write("/\3\60\3\60\3\60\3\60\3\60\5\60\u01cd\n\60\3\61\3\61\3")
        buf.write("\62\3\62\3\62\5\62\u01d4\n\62\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\2\7>@FJN\65\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@")
        buf.write("BDFHJLNPRTVXZ\\^`bdf\2\5\3\2\31\32\6\2\22\23\25\26.\60")
        buf.write("\64\64\7\2\3\3\n\n\f\f\16\16\64\64\2\u01e3\2k\3\2\2\2")
        buf.write("\4p\3\2\2\2\6\u0081\3\2\2\2\b\u0085\3\2\2\2\n\u0088\3")
        buf.write("\2\2\2\f\u0094\3\2\2\2\16\u0096\3\2\2\2\20\u009d\3\2\2")
        buf.write("\2\22\u00a4\3\2\2\2\24\u00b7\3\2\2\2\26\u00b9\3\2\2\2")
        buf.write("\30\u00bc\3\2\2\2\32\u00c5\3\2\2\2\34\u00c9\3\2\2\2\36")
        buf.write("\u00cb\3\2\2\2 \u00d6\3\2\2\2\"\u00e0\3\2\2\2$\u00e8\3")
        buf.write("\2\2\2&\u00ea\3\2\2\2(\u00f0\3\2\2\2*\u00f6\3\2\2\2,\u00f8")
        buf.write("\3\2\2\2.\u0100\3\2\2\2\60\u010c\3\2\2\2\62\u010e\3\2")
        buf.write("\2\2\64\u0113\3\2\2\2\66\u0127\3\2\2\28\u0129\3\2\2\2")
        buf.write(":\u012c\3\2\2\2<\u012f\3\2\2\2>\u0133\3\2\2\2@\u013e\3")
        buf.write("\2\2\2B\u014e\3\2\2\2D\u0155\3\2\2\2F\u0157\3\2\2\2H\u0165")
        buf.write("\3\2\2\2J\u0167\3\2\2\2L\u0178\3\2\2\2N\u017a\3\2\2\2")
        buf.write("P\u0193\3\2\2\2R\u019a\3\2\2\2T\u01a1\3\2\2\2V\u01a6\3")
        buf.write("\2\2\2X\u01a8\3\2\2\2Z\u01ae\3\2\2\2\\\u01c5\3\2\2\2^")
        buf.write("\u01cc\3\2\2\2`\u01ce\3\2\2\2b\u01d3\3\2\2\2d\u01d5\3")
        buf.write("\2\2\2f\u01da\3\2\2\2hj\5\4\3\2ih\3\2\2\2jm\3\2\2\2ki")
        buf.write("\3\2\2\2kl\3\2\2\2ln\3\2\2\2mk\3\2\2\2no\7\2\2\3o\3\3")
        buf.write("\2\2\2pq\7\5\2\2qt\7\64\2\2rs\7\t\2\2su\7\64\2\2tr\3\2")
        buf.write("\2\2tu\3\2\2\2uv\3\2\2\2vz\7(\2\2wy\5\6\4\2xw\3\2\2\2")
        buf.write("y|\3\2\2\2zx\3\2\2\2z{\3\2\2\2{}\3\2\2\2|z\3\2\2\2}~\7")
        buf.write(")\2\2~\5\3\2\2\2\177\u0082\5\b\5\2\u0080\u0082\5\34\17")
        buf.write("\2\u0081\177\3\2\2\2\u0081\u0080\3\2\2\2\u0082\7\3\2\2")
        buf.write("\2\u0083\u0086\5\n\6\2\u0084\u0086\5\24\13\2\u0085\u0083")
        buf.write("\3\2\2\2\u0085\u0084\3\2\2\2\u0086\t\3\2\2\2\u0087\u0089")
        buf.write("\7\30\2\2\u0088\u0087\3\2\2\2\u0088\u0089\3\2\2\2\u0089")
        buf.write("\u008a\3\2\2\2\u008a\u008b\5\f\7\2\u008b\u008c\5\16\b")
        buf.write("\2\u008c\u008d\7*\2\2\u008d\13\3\2\2\2\u008e\u0095\7\f")
        buf.write("\2\2\u008f\u0095\7\n\2\2\u0090\u0095\7\3\2\2\u0091\u0095")
        buf.write("\7\16\2\2\u0092\u0095\7\64\2\2\u0093\u0095\5f\64\2\u0094")
        buf.write("\u008e\3\2\2\2\u0094\u008f\3\2\2\2\u0094\u0090\3\2\2\2")
        buf.write("\u0094\u0091\3\2\2\2\u0094\u0092\3\2\2\2\u0094\u0093\3")
        buf.write("\2\2\2\u0095\r\3\2\2\2\u0096\u0097\5\20\t\2\u0097\u0098")
        buf.write("\5\22\n\2\u0098\17\3\2\2\2\u0099\u009a\7\64\2\2\u009a")
        buf.write("\u009b\7#\2\2\u009b\u009e\5> \2\u009c\u009e\7\64\2\2\u009d")
        buf.write("\u0099\3\2\2\2\u009d\u009c\3\2\2\2\u009e\21\3\2\2\2\u009f")
        buf.write("\u00a0\7-\2\2\u00a0\u00a1\5\20\t\2\u00a1\u00a2\5\22\n")
        buf.write("\2\u00a2\u00a5\3\2\2\2\u00a3\u00a5\3\2\2\2\u00a4\u009f")
        buf.write("\3\2\2\2\u00a4\u00a3\3\2\2\2\u00a5\23\3\2\2\2\u00a6\u00a7")
        buf.write("\7\27\2\2\u00a7\u00a8\5\f\7\2\u00a8\u00a9\5\26\f\2\u00a9")
        buf.write("\u00aa\7*\2\2\u00aa\u00b8\3\2\2\2\u00ab\u00ac\7\27\2\2")
        buf.write("\u00ac\u00ad\7\30\2\2\u00ad\u00ae\5\f\7\2\u00ae\u00af")
        buf.write("\5\26\f\2\u00af\u00b0\7*\2\2\u00b0\u00b8\3\2\2\2\u00b1")
        buf.write("\u00b2\7\30\2\2\u00b2\u00b3\7\27\2\2\u00b3\u00b4\5\f\7")
        buf.write("\2\u00b4\u00b5\5\26\f\2\u00b5\u00b6\7*\2\2\u00b6\u00b8")
        buf.write("\3\2\2\2\u00b7\u00a6\3\2\2\2\u00b7\u00ab\3\2\2\2\u00b7")
        buf.write("\u00b1\3\2\2\2\u00b8\25\3\2\2\2\u00b9\u00ba\5\30\r\2\u00ba")
        buf.write("\u00bb\5\32\16\2\u00bb\27\3\2\2\2\u00bc\u00bd\7\64\2\2")
        buf.write("\u00bd\u00be\7#\2\2\u00be\u00bf\5> \2\u00bf\31\3\2\2\2")
        buf.write("\u00c0\u00c1\7-\2\2\u00c1\u00c2\5\30\r\2\u00c2\u00c3\5")
        buf.write("\32\16\2\u00c3\u00c6\3\2\2\2\u00c4\u00c6\3\2\2\2\u00c5")
        buf.write("\u00c0\3\2\2\2\u00c5\u00c4\3\2\2\2\u00c6\33\3\2\2\2\u00c7")
        buf.write("\u00ca\5\36\20\2\u00c8\u00ca\5 \21\2\u00c9\u00c7\3\2\2")
        buf.write("\2\u00c9\u00c8\3\2\2\2\u00ca\35\3\2\2\2\u00cb\u00cc\7")
        buf.write("\30\2\2\u00cc\u00cd\5(\25\2\u00cd\u00ce\7\64\2\2\u00ce")
        buf.write("\u00d0\7$\2\2\u00cf\u00d1\5\"\22\2\u00d0\u00cf\3\2\2\2")
        buf.write("\u00d0\u00d1\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d3\7")
        buf.write("%\2\2\u00d3\u00d4\5,\27\2\u00d4\37\3\2\2\2\u00d5\u00d7")
        buf.write("\5(\25\2\u00d6\u00d5\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7")
        buf.write("\u00d8\3\2\2\2\u00d8\u00d9\7\64\2\2\u00d9\u00db\7$\2\2")
        buf.write("\u00da\u00dc\5\"\22\2\u00db\u00da\3\2\2\2\u00db\u00dc")
        buf.write("\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00de\7%\2\2\u00de")
        buf.write("\u00df\5,\27\2\u00df!\3\2\2\2\u00e0\u00e1\5&\24\2\u00e1")
        buf.write("\u00e2\5$\23\2\u00e2#\3\2\2\2\u00e3\u00e4\7*\2\2\u00e4")
        buf.write("\u00e5\5&\24\2\u00e5\u00e6\5$\23\2\u00e6\u00e9\3\2\2\2")
        buf.write("\u00e7\u00e9\3\2\2\2\u00e8\u00e3\3\2\2\2\u00e8\u00e7\3")
        buf.write("\2\2\2\u00e9%\3\2\2\2\u00ea\u00eb\5\f\7\2\u00eb\u00ec")
        buf.write("\7\64\2\2\u00ec\u00ed\5*\26\2\u00ed\'\3\2\2\2\u00ee\u00f1")
        buf.write("\5\f\7\2\u00ef\u00f1\7\24\2\2\u00f0\u00ee\3\2\2\2\u00f0")
        buf.write("\u00ef\3\2\2\2\u00f1)\3\2\2\2\u00f2\u00f3\7-\2\2\u00f3")
        buf.write("\u00f4\7\64\2\2\u00f4\u00f7\5*\26\2\u00f5\u00f7\3\2\2")
        buf.write("\2\u00f6\u00f2\3\2\2\2\u00f6\u00f5\3\2\2\2\u00f7+\3\2")
        buf.write("\2\2\u00f8\u00f9\7(\2\2\u00f9\u00fa\5.\30\2\u00fa\u00fb")
        buf.write("\7)\2\2\u00fb-\3\2\2\2\u00fc\u00fd\5\60\31\2\u00fd\u00fe")
        buf.write("\5.\30\2\u00fe\u0101\3\2\2\2\u00ff\u0101\3\2\2\2\u0100")
        buf.write("\u00fc\3\2\2\2\u0100\u00ff\3\2\2\2\u0101/\3\2\2\2\u0102")
        buf.write("\u010d\5\b\5\2\u0103\u010d\5\62\32\2\u0104\u010d\5\66")
        buf.write("\34\2\u0105\u010d\5\64\33\2\u0106\u010d\58\35\2\u0107")
        buf.write("\u010d\5:\36\2\u0108\u010d\5<\37\2\u0109\u010a\5> \2\u010a")
        buf.write("\u010b\7*\2\2\u010b\u010d\3\2\2\2\u010c\u0102\3\2\2\2")
        buf.write("\u010c\u0103\3\2\2\2\u010c\u0104\3\2\2\2\u010c\u0105\3")
        buf.write("\2\2\2\u010c\u0106\3\2\2\2\u010c\u0107\3\2\2\2\u010c\u0108")
        buf.write("\3\2\2\2\u010c\u0109\3\2\2\2\u010d\61\3\2\2\2\u010e\u010f")
        buf.write("\5b\62\2\u010f\u0110\7\"\2\2\u0110\u0111\5> \2\u0111\u0112")
        buf.write("\7*\2\2\u0112\63\3\2\2\2\u0113\u0114\7\20\2\2\u0114\u0115")
        buf.write("\5`\61\2\u0115\u0116\7\"\2\2\u0116\u0117\5> \2\u0117\u0118")
        buf.write("\t\2\2\2\u0118\u0119\5> \2\u0119\u011c\7\7\2\2\u011a\u011d")
        buf.write("\5\60\31\2\u011b\u011d\5\66\34\2\u011c\u011a\3\2\2\2\u011c")
        buf.write("\u011b\3\2\2\2\u011d\65\3\2\2\2\u011e\u011f\7\13\2\2\u011f")
        buf.write("\u0120\5> \2\u0120\u0121\7\17\2\2\u0121\u0124\5\60\31")
        buf.write("\2\u0122\u0123\7\b\2\2\u0123\u0125\5\60\31\2\u0124\u0122")
        buf.write("\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u0128\3\2\2\2\u0126")
        buf.write("\u0128\5,\27\2\u0127\u011e\3\2\2\2\u0127\u0126\3\2\2\2")
        buf.write("\u0128\67\3\2\2\2\u0129\u012a\7\4\2\2\u012a\u012b\7*\2")
        buf.write("\2\u012b9\3\2\2\2\u012c\u012d\7\6\2\2\u012d\u012e\7*\2")
        buf.write("\2\u012e;\3\2\2\2\u012f\u0130\7\21\2\2\u0130\u0131\5>")
        buf.write(" \2\u0131\u0132\7*\2\2\u0132=\3\2\2\2\u0133\u0134\b \1")
        buf.write("\2\u0134\u0135\5@!\2\u0135\u013b\3\2\2\2\u0136\u0137\f")
        buf.write("\4\2\2\u0137\u0138\7\33\2\2\u0138\u013a\5@!\2\u0139\u0136")
        buf.write("\3\2\2\2\u013a\u013d\3\2\2\2\u013b\u0139\3\2\2\2\u013b")
        buf.write("\u013c\3\2\2\2\u013c?\3\2\2\2\u013d\u013b\3\2\2\2\u013e")
        buf.write("\u013f\b!\1\2\u013f\u0140\5B\"\2\u0140\u0146\3\2\2\2\u0141")
        buf.write("\u0142\f\4\2\2\u0142\u0143\7\34\2\2\u0143\u0145\5B\"\2")
        buf.write("\u0144\u0141\3\2\2\2\u0145\u0148\3\2\2\2\u0146\u0144\3")
        buf.write("\2\2\2\u0146\u0147\3\2\2\2\u0147A\3\2\2\2\u0148\u0146")
        buf.write("\3\2\2\2\u0149\u014a\5D#\2\u014a\u014b\7\35\2\2\u014b")
        buf.write("\u014c\5D#\2\u014c\u014f\3\2\2\2\u014d\u014f\5D#\2\u014e")
        buf.write("\u0149\3\2\2\2\u014e\u014d\3\2\2\2\u014fC\3\2\2\2\u0150")
        buf.write("\u0151\5F$\2\u0151\u0152\7\36\2\2\u0152\u0153\5F$\2\u0153")
        buf.write("\u0156\3\2\2\2\u0154\u0156\5F$\2\u0155\u0150\3\2\2\2\u0155")
        buf.write("\u0154\3\2\2\2\u0156E\3\2\2\2\u0157\u0158\b$\1\2\u0158")
        buf.write("\u0159\5H%\2\u0159\u015f\3\2\2\2\u015a\u015b\f\4\2\2\u015b")
        buf.write("\u015c\7\37\2\2\u015c\u015e\5H%\2\u015d\u015a\3\2\2\2")
        buf.write("\u015e\u0161\3\2\2\2\u015f\u015d\3\2\2\2\u015f\u0160\3")
        buf.write("\2\2\2\u0160G\3\2\2\2\u0161\u015f\3\2\2\2\u0162\u0163")
        buf.write("\7 \2\2\u0163\u0166\5H%\2\u0164\u0166\5J&\2\u0165\u0162")
        buf.write("\3\2\2\2\u0165\u0164\3\2\2\2\u0166I\3\2\2\2\u0167\u0168")
        buf.write("\b&\1\2\u0168\u0169\5L\'\2\u0169\u016f\3\2\2\2\u016a\u016b")
        buf.write("\f\4\2\2\u016b\u016c\7!\2\2\u016c\u016e\5L\'\2\u016d\u016a")
        buf.write("\3\2\2\2\u016e\u0171\3\2\2\2\u016f\u016d\3\2\2\2\u016f")
        buf.write("\u0170\3\2\2\2\u0170K\3\2\2\2\u0171\u016f\3\2\2\2\u0172")
        buf.write("\u0173\5N(\2\u0173\u0174\7&\2\2\u0174\u0175\5> \2\u0175")
        buf.write("\u0176\7\'\2\2\u0176\u0179\3\2\2\2\u0177\u0179\5N(\2\u0178")
        buf.write("\u0172\3\2\2\2\u0178\u0177\3\2\2\2\u0179M\3\2\2\2\u017a")
        buf.write("\u017b\b(\1\2\u017b\u017c\5P)\2\u017c\u0189\3\2\2\2\u017d")
        buf.write("\u017e\f\5\2\2\u017e\u017f\7,\2\2\u017f\u0188\7\64\2\2")
        buf.write("\u0180\u0181\f\4\2\2\u0181\u0182\7,\2\2\u0182\u0183\7")
        buf.write("\64\2\2\u0183\u0184\7$\2\2\u0184\u0185\5Z.\2\u0185\u0186")
        buf.write("\7%\2\2\u0186\u0188\3\2\2\2\u0187\u017d\3\2\2\2\u0187")
        buf.write("\u0180\3\2\2\2\u0188\u018b\3\2\2\2\u0189\u0187\3\2\2\2")
        buf.write("\u0189\u018a\3\2\2\2\u018aO\3\2\2\2\u018b\u0189\3\2\2")
        buf.write("\2\u018c\u018d\7\r\2\2\u018d\u018e\7\64\2\2\u018e\u018f")
        buf.write("\7$\2\2\u018f\u0190\5Z.\2\u0190\u0191\7%\2\2\u0191\u0194")
        buf.write("\3\2\2\2\u0192\u0194\5R*\2\u0193\u018c\3\2\2\2\u0193\u0192")
        buf.write("\3\2\2\2\u0194Q\3\2\2\2\u0195\u0196\7(\2\2\u0196\u0197")
        buf.write("\5Z.\2\u0197\u0198\7)\2\2\u0198\u019b\3\2\2\2\u0199\u019b")
        buf.write("\5T+\2\u019a\u0195\3\2\2\2\u019a\u0199\3\2\2\2\u019bS")
        buf.write("\3\2\2\2\u019c\u019d\7$\2\2\u019d\u019e\5> \2\u019e\u019f")
        buf.write("\7%\2\2\u019f\u01a2\3\2\2\2\u01a0\u01a2\5V,\2\u01a1\u019c")
        buf.write("\3\2\2\2\u01a1\u01a0\3\2\2\2\u01a2U\3\2\2\2\u01a3\u01a4")
        buf.write("\7\33\2\2\u01a4\u01a7\5V,\2\u01a5\u01a7\5X-\2\u01a6\u01a3")
        buf.write("\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7W\3\2\2\2\u01a8\u01a9")
        buf.write("\t\3\2\2\u01a9Y\3\2\2\2\u01aa\u01ab\5> \2\u01ab\u01ac")
        buf.write("\5^\60\2\u01ac\u01af\3\2\2\2\u01ad\u01af\3\2\2\2\u01ae")
        buf.write("\u01aa\3\2\2\2\u01ae\u01ad\3\2\2\2\u01af[\3\2\2\2\u01b0")
        buf.write("\u01b1\5> \2\u01b1\u01b2\7,\2\2\u01b2\u01b3\7\64\2\2\u01b3")
        buf.write("\u01c6\3\2\2\2\u01b4\u01b5\5> \2\u01b5\u01b6\7,\2\2\u01b6")
        buf.write("\u01b7\7\64\2\2\u01b7\u01b8\7$\2\2\u01b8\u01b9\5Z.\2\u01b9")
        buf.write("\u01ba\7%\2\2\u01ba\u01c6\3\2\2\2\u01bb\u01bc\7\64\2\2")
        buf.write("\u01bc\u01bd\7,\2\2\u01bd\u01c6\7\64\2\2\u01be\u01bf\7")
        buf.write("\64\2\2\u01bf\u01c0\7,\2\2\u01c0\u01c1\7\64\2\2\u01c1")
        buf.write("\u01c2\7$\2\2\u01c2\u01c3\5Z.\2\u01c3\u01c4\7%\2\2\u01c4")
        buf.write("\u01c6\3\2\2\2\u01c5\u01b0\3\2\2\2\u01c5\u01b4\3\2\2\2")
        buf.write("\u01c5\u01bb\3\2\2\2\u01c5\u01be\3\2\2\2\u01c6]\3\2\2")
        buf.write("\2\u01c7\u01c8\7-\2\2\u01c8\u01c9\5> \2\u01c9\u01ca\5")
        buf.write("^\60\2\u01ca\u01cd\3\2\2\2\u01cb\u01cd\3\2\2\2\u01cc\u01c7")
        buf.write("\3\2\2\2\u01cc\u01cb\3\2\2\2\u01cd_\3\2\2\2\u01ce\u01cf")
        buf.write("\7\64\2\2\u01cfa\3\2\2\2\u01d0\u01d4\7\64\2\2\u01d1\u01d4")
        buf.write("\5d\63\2\u01d2\u01d4\5\\/\2\u01d3\u01d0\3\2\2\2\u01d3")
        buf.write("\u01d1\3\2\2\2\u01d3\u01d2\3\2\2\2\u01d4c\3\2\2\2\u01d5")
        buf.write("\u01d6\5> \2\u01d6\u01d7\7&\2\2\u01d7\u01d8\5> \2\u01d8")
        buf.write("\u01d9\7\'\2\2\u01d9e\3\2\2\2\u01da\u01db\t\4\2\2\u01db")
        buf.write("\u01dc\7&\2\2\u01dc\u01dd\7.\2\2\u01dd\u01de\7\'\2\2\u01de")
        buf.write("g\3\2\2\2+ktz\u0081\u0085\u0088\u0094\u009d\u00a4\u00b7")
        buf.write("\u00c5\u00c9\u00d0\u00d6\u00db\u00e8\u00f0\u00f6\u0100")
        buf.write("\u010c\u011c\u0124\u0127\u013b\u0146\u014e\u0155\u015f")
        buf.write("\u0165\u016f\u0178\u0187\u0189\u0193\u019a\u01a1\u01a6")
        buf.write("\u01ae\u01c5\u01cc\u01d3")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'boolean'", "'break'", "'class'", "'continue'", 
                     "'do'", "'else'", "'extends'", "'float'", "'if'", "'int'", 
                     "'new'", "'string'", "'then'", "'for'", "'return'", 
                     "'true'", "'false'", "'void'", "'nil'", "'this'", "'final'", 
                     "'static'", "'to'", "'downto'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'!'", "'^'", 
                     "':='", "'='", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "';'", "':'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>", "BOOLEAN", "BREAK", "CLASS", "CONTINUE", 
                      "DO", "ELSE", "EXTENDS", "FLOAT", "IF", "INT", "NEW", 
                      "STRING", "THEN", "FOR", "RETURN", "TRUE", "FALSE", 
                      "VOID", "NIL", "THIS", "FINAL", "STATIC", "TO", "DOWNTO", 
                      "OP0", "OP1", "OP2", "OP3", "OP4", "NOT", "CONCAT", 
                      "ASSIGN", "INITASSIGN", "LB", "RB", "LSB", "RSB", 
                      "LP", "RP", "SEMI", "CL", "DOT", "COMMA", "INTLIT", 
                      "FLOATLIT", "STRLIT", "WS", "COMMENT", "LINECOMMENT", 
                      "ID", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_classdecl = 1
    RULE_memberdecl = 2
    RULE_attributedecl = 3
    RULE_vardecl = 4
    RULE_typ = 5
    RULE_attrlist = 6
    RULE_attrname = 7
    RULE_subattrlist = 8
    RULE_constdecl = 9
    RULE_constattrlist = 10
    RULE_constattr = 11
    RULE_subconstattrlist = 12
    RULE_methoddecl = 13
    RULE_staticmethods = 14
    RULE_instancemethods = 15
    RULE_paramlist = 16
    RULE_subparamlist = 17
    RULE_param = 18
    RULE_returntype = 19
    RULE_idlist = 20
    RULE_blockstmt = 21
    RULE_stmtlist = 22
    RULE_stmt = 23
    RULE_assignstmt = 24
    RULE_forstmt = 25
    RULE_ifstmt = 26
    RULE_breakstmt = 27
    RULE_continuestmt = 28
    RULE_returnstmt = 29
    RULE_expr = 30
    RULE_expr1 = 31
    RULE_expr2 = 32
    RULE_expr3 = 33
    RULE_expr4 = 34
    RULE_expr5 = 35
    RULE_expr6 = 36
    RULE_expr7 = 37
    RULE_expr8 = 38
    RULE_expr9 = 39
    RULE_expr10 = 40
    RULE_expr11 = 41
    RULE_expr12 = 42
    RULE_operands = 43
    RULE_exprlist = 44
    RULE_fieldaccess = 45
    RULE_argumentslist = 46
    RULE_scalarvar = 47
    RULE_lhs = 48
    RULE_arraycell = 49
    RULE_arraytype = 50

    ruleNames =  [ "program", "classdecl", "memberdecl", "attributedecl", 
                   "vardecl", "typ", "attrlist", "attrname", "subattrlist", 
                   "constdecl", "constattrlist", "constattr", "subconstattrlist", 
                   "methoddecl", "staticmethods", "instancemethods", "paramlist", 
                   "subparamlist", "param", "returntype", "idlist", "blockstmt", 
                   "stmtlist", "stmt", "assignstmt", "forstmt", "ifstmt", 
                   "breakstmt", "continuestmt", "returnstmt", "expr", "expr1", 
                   "expr2", "expr3", "expr4", "expr5", "expr6", "expr7", 
                   "expr8", "expr9", "expr10", "expr11", "expr12", "operands", 
                   "exprlist", "fieldaccess", "argumentslist", "scalarvar", 
                   "lhs", "arraycell", "arraytype" ]

    EOF = Token.EOF
    BOOLEAN=1
    BREAK=2
    CLASS=3
    CONTINUE=4
    DO=5
    ELSE=6
    EXTENDS=7
    FLOAT=8
    IF=9
    INT=10
    NEW=11
    STRING=12
    THEN=13
    FOR=14
    RETURN=15
    TRUE=16
    FALSE=17
    VOID=18
    NIL=19
    THIS=20
    FINAL=21
    STATIC=22
    TO=23
    DOWNTO=24
    OP0=25
    OP1=26
    OP2=27
    OP3=28
    OP4=29
    NOT=30
    CONCAT=31
    ASSIGN=32
    INITASSIGN=33
    LB=34
    RB=35
    LSB=36
    RSB=37
    LP=38
    RP=39
    SEMI=40
    CL=41
    DOT=42
    COMMA=43
    INTLIT=44
    FLOATLIT=45
    STRLIT=46
    WS=47
    COMMENT=48
    LINECOMMENT=49
    ID=50
    ERROR_CHAR=51
    UNCLOSE_STRING=52
    ILLEGAL_ESCAPE=53

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def classdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ClassdeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ClassdeclContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.CLASS:
                self.state = 102
                self.classdecl()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 108
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(BKOOLParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def EXTENDS(self):
            return self.getToken(BKOOLParser.EXTENDS, 0)

        def memberdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.MemberdeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.MemberdeclContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_classdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassdecl" ):
                return visitor.visitClassdecl(self)
            else:
                return visitor.visitChildren(self)




    def classdecl(self):

        localctx = BKOOLParser.ClassdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(BKOOLParser.CLASS)
            self.state = 111
            self.match(BKOOLParser.ID)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 112
                self.match(BKOOLParser.EXTENDS)
                self.state = 113
                self.match(BKOOLParser.ID)


            self.state = 116
            self.match(BKOOLParser.LP)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.ID))) != 0):
                self.state = 117
                self.memberdecl()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 123
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributedecl(self):
            return self.getTypedRuleContext(BKOOLParser.AttributedeclContext,0)


        def methoddecl(self):
            return self.getTypedRuleContext(BKOOLParser.MethoddeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_memberdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberdecl" ):
                return visitor.visitMemberdecl(self)
            else:
                return visitor.visitChildren(self)




    def memberdecl(self):

        localctx = BKOOLParser.MemberdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_memberdecl)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.attributedecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.methoddecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(BKOOLParser.ConstdeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attributedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributedecl" ):
                return visitor.visitAttributedecl(self)
            else:
                return visitor.visitChildren(self)




    def attributedecl(self):

        localctx = BKOOLParser.AttributedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attributedecl)
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.constdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def attrlist(self):
            return self.getTypedRuleContext(BKOOLParser.AttrlistContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = BKOOLParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 133
                self.match(BKOOLParser.STATIC)


            self.state = 136
            self.typ()
            self.state = 137
            self.attrlist()
            self.state = 138
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def arraytype(self):
            return self.getTypedRuleContext(BKOOLParser.ArraytypeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = BKOOLParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_typ)
        try:
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.match(BKOOLParser.INT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.match(BKOOLParser.FLOAT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 142
                self.match(BKOOLParser.BOOLEAN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 143
                self.match(BKOOLParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 144
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 145
                self.arraytype()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attrname(self):
            return self.getTypedRuleContext(BKOOLParser.AttrnameContext,0)


        def subattrlist(self):
            return self.getTypedRuleContext(BKOOLParser.SubattrlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attrlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrlist" ):
                return visitor.visitAttrlist(self)
            else:
                return visitor.visitChildren(self)




    def attrlist(self):

        localctx = BKOOLParser.AttrlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attrlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.attrname()
            self.state = 149
            self.subattrlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrnameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def INITASSIGN(self):
            return self.getToken(BKOOLParser.INITASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attrname

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrname" ):
                return visitor.visitAttrname(self)
            else:
                return visitor.visitChildren(self)




    def attrname(self):

        localctx = BKOOLParser.AttrnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attrname)
        try:
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.match(BKOOLParser.ID)
                self.state = 152
                self.match(BKOOLParser.INITASSIGN)
                self.state = 153
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubattrlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def attrname(self):
            return self.getTypedRuleContext(BKOOLParser.AttrnameContext,0)


        def subattrlist(self):
            return self.getTypedRuleContext(BKOOLParser.SubattrlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_subattrlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubattrlist" ):
                return visitor.visitSubattrlist(self)
            else:
                return visitor.visitChildren(self)




    def subattrlist(self):

        localctx = BKOOLParser.SubattrlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_subattrlist)
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.match(BKOOLParser.COMMA)
                self.state = 158
                self.attrname()
                self.state = 159
                self.subattrlist()
                pass
            elif token in [BKOOLParser.SEMI]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def constattrlist(self):
            return self.getTypedRuleContext(BKOOLParser.ConstattrlistContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_constdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstdecl" ):
                return visitor.visitConstdecl(self)
            else:
                return visitor.visitChildren(self)




    def constdecl(self):

        localctx = BKOOLParser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_constdecl)
        try:
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.match(BKOOLParser.FINAL)
                self.state = 165
                self.typ()
                self.state = 166
                self.constattrlist()
                self.state = 167
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.match(BKOOLParser.FINAL)
                self.state = 170
                self.match(BKOOLParser.STATIC)
                self.state = 171
                self.typ()
                self.state = 172
                self.constattrlist()
                self.state = 173
                self.match(BKOOLParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 175
                self.match(BKOOLParser.STATIC)
                self.state = 176
                self.match(BKOOLParser.FINAL)
                self.state = 177
                self.typ()
                self.state = 178
                self.constattrlist()
                self.state = 179
                self.match(BKOOLParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstattrlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constattr(self):
            return self.getTypedRuleContext(BKOOLParser.ConstattrContext,0)


        def subconstattrlist(self):
            return self.getTypedRuleContext(BKOOLParser.SubconstattrlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_constattrlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstattrlist" ):
                return visitor.visitConstattrlist(self)
            else:
                return visitor.visitChildren(self)




    def constattrlist(self):

        localctx = BKOOLParser.ConstattrlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_constattrlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.constattr()
            self.state = 184
            self.subconstattrlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstattrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def INITASSIGN(self):
            return self.getToken(BKOOLParser.INITASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_constattr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstattr" ):
                return visitor.visitConstattr(self)
            else:
                return visitor.visitChildren(self)




    def constattr(self):

        localctx = BKOOLParser.ConstattrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_constattr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(BKOOLParser.ID)
            self.state = 187
            self.match(BKOOLParser.INITASSIGN)
            self.state = 188
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubconstattrlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def constattr(self):
            return self.getTypedRuleContext(BKOOLParser.ConstattrContext,0)


        def subconstattrlist(self):
            return self.getTypedRuleContext(BKOOLParser.SubconstattrlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_subconstattrlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubconstattrlist" ):
                return visitor.visitSubconstattrlist(self)
            else:
                return visitor.visitChildren(self)




    def subconstattrlist(self):

        localctx = BKOOLParser.SubconstattrlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_subconstattrlist)
        try:
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.match(BKOOLParser.COMMA)
                self.state = 191
                self.constattr()
                self.state = 192
                self.subconstattrlist()
                pass
            elif token in [BKOOLParser.SEMI]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethoddeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def staticmethods(self):
            return self.getTypedRuleContext(BKOOLParser.StaticmethodsContext,0)


        def instancemethods(self):
            return self.getTypedRuleContext(BKOOLParser.InstancemethodsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_methoddecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethoddecl" ):
                return visitor.visitMethoddecl(self)
            else:
                return visitor.visitChildren(self)




    def methoddecl(self):

        localctx = BKOOLParser.MethoddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_methoddecl)
        try:
            self.state = 199
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.STATIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.staticmethods()
                pass
            elif token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.instancemethods()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaticmethodsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def returntype(self):
            return self.getTypedRuleContext(BKOOLParser.ReturntypeContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(BKOOLParser.BlockstmtContext,0)


        def paramlist(self):
            return self.getTypedRuleContext(BKOOLParser.ParamlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_staticmethods

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStaticmethods" ):
                return visitor.visitStaticmethods(self)
            else:
                return visitor.visitChildren(self)




    def staticmethods(self):

        localctx = BKOOLParser.StaticmethodsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_staticmethods)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(BKOOLParser.STATIC)
            self.state = 202
            self.returntype()
            self.state = 203
            self.match(BKOOLParser.ID)
            self.state = 204
            self.match(BKOOLParser.LB)
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0):
                self.state = 205
                self.paramlist()


            self.state = 208
            self.match(BKOOLParser.RB)
            self.state = 209
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstancemethodsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(BKOOLParser.BlockstmtContext,0)


        def returntype(self):
            return self.getTypedRuleContext(BKOOLParser.ReturntypeContext,0)


        def paramlist(self):
            return self.getTypedRuleContext(BKOOLParser.ParamlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_instancemethods

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstancemethods" ):
                return visitor.visitInstancemethods(self)
            else:
                return visitor.visitChildren(self)




    def instancemethods(self):

        localctx = BKOOLParser.InstancemethodsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_instancemethods)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 211
                self.returntype()


            self.state = 214
            self.match(BKOOLParser.ID)
            self.state = 215
            self.match(BKOOLParser.LB)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0):
                self.state = 216
                self.paramlist()


            self.state = 219
            self.match(BKOOLParser.RB)
            self.state = 220
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(BKOOLParser.ParamContext,0)


        def subparamlist(self):
            return self.getTypedRuleContext(BKOOLParser.SubparamlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = BKOOLParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_paramlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.param()
            self.state = 223
            self.subparamlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubparamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def param(self):
            return self.getTypedRuleContext(BKOOLParser.ParamContext,0)


        def subparamlist(self):
            return self.getTypedRuleContext(BKOOLParser.SubparamlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_subparamlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubparamlist" ):
                return visitor.visitSubparamlist(self)
            else:
                return visitor.visitChildren(self)




    def subparamlist(self):

        localctx = BKOOLParser.SubparamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_subparamlist)
        try:
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.SEMI]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.match(BKOOLParser.SEMI)
                self.state = 226
                self.param()
                self.state = 227
                self.subparamlist()
                pass
            elif token in [BKOOLParser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = BKOOLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.typ()
            self.state = 233
            self.match(BKOOLParser.ID)
            self.state = 234
            self.idlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturntypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_returntype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturntype" ):
                return visitor.visitReturntype(self)
            else:
                return visitor.visitChildren(self)




    def returntype(self):

        localctx = BKOOLParser.ReturntypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_returntype)
        try:
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.typ()
                pass
            elif token in [BKOOLParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.match(BKOOLParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = BKOOLParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_idlist)
        try:
            self.state = 244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.match(BKOOLParser.COMMA)
                self.state = 241
                self.match(BKOOLParser.ID)
                self.state = 242
                self.idlist()
                pass
            elif token in [BKOOLParser.RB, BKOOLParser.SEMI]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(BKOOLParser.StmtlistContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_blockstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = BKOOLParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(BKOOLParser.LP)
            self.state = 247
            self.stmtlist()
            self.state = 248
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(BKOOLParser.StmtlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




    def stmtlist(self):

        localctx = BKOOLParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_stmtlist)
        try:
            self.state = 254
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.BREAK, BKOOLParser.CONTINUE, BKOOLParser.FLOAT, BKOOLParser.IF, BKOOLParser.INT, BKOOLParser.NEW, BKOOLParser.STRING, BKOOLParser.FOR, BKOOLParser.RETURN, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.FINAL, BKOOLParser.STATIC, BKOOLParser.OP0, BKOOLParser.NOT, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.stmt()
                self.state = 251
                self.stmtlist()
                pass
            elif token in [BKOOLParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributedecl(self):
            return self.getTypedRuleContext(BKOOLParser.AttributedeclContext,0)


        def assignstmt(self):
            return self.getTypedRuleContext(BKOOLParser.AssignstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(BKOOLParser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(BKOOLParser.ForstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(BKOOLParser.BreakstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(BKOOLParser.ContinuestmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(BKOOLParser.ReturnstmtContext,0)


        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_stmt)
        try:
            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.attributedecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.assignstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 258
                self.ifstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 259
                self.forstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 260
                self.breakstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 261
                self.continuestmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 262
                self.returnstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 263
                self.expr(0)
                self.state = 264
                self.match(BKOOLParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(BKOOLParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = BKOOLParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_assignstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.lhs()
            self.state = 269
            self.match(BKOOLParser.ASSIGN)
            self.state = 270
            self.expr(0)
            self.state = 271
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKOOLParser.FOR, 0)

        def scalarvar(self):
            return self.getTypedRuleContext(BKOOLParser.ScalarvarContext,0)


        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(BKOOLParser.IfstmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = BKOOLParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_forstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(BKOOLParser.FOR)
            self.state = 274
            self.scalarvar()
            self.state = 275
            self.match(BKOOLParser.ASSIGN)
            self.state = 276
            self.expr(0)
            self.state = 277
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 278
            self.expr(0)
            self.state = 279
            self.match(BKOOLParser.DO)
            self.state = 282
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 280
                self.stmt()
                pass

            elif la_ == 2:
                self.state = 281
                self.ifstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def THEN(self):
            return self.getToken(BKOOLParser.THEN, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmtContext,i)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(BKOOLParser.BlockstmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = BKOOLParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_ifstmt)
        try:
            self.state = 293
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.match(BKOOLParser.IF)
                self.state = 285
                self.expr(0)
                self.state = 286
                self.match(BKOOLParser.THEN)
                self.state = 287
                self.stmt()
                self.state = 290
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 288
                    self.match(BKOOLParser.ELSE)
                    self.state = 289
                    self.stmt()


                pass
            elif token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 292
                self.blockstmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = BKOOLParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(BKOOLParser.BREAK)
            self.state = 296
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKOOLParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_continuestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




    def continuestmt(self):

        localctx = BKOOLParser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(BKOOLParser.CONTINUE)
            self.state = 299
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = BKOOLParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_returnstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(BKOOLParser.RETURN)
            self.state = 302
            self.expr(0)
            self.state = 303
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(BKOOLParser.Expr1Context,0)


        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def OP0(self):
            return self.getToken(BKOOLParser.OP0, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 313
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 308
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 309
                    self.match(BKOOLParser.OP0)
                    self.state = 310
                    self.expr1(0) 
                self.state = 315
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(BKOOLParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(BKOOLParser.Expr1Context,0)


        def OP1(self):
            return self.getToken(BKOOLParser.OP1, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.expr2()
            self._ctx.stop = self._input.LT(-1)
            self.state = 324
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 319
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 320
                    self.match(BKOOLParser.OP1)
                    self.state = 321
                    self.expr2() 
                self.state = 326
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Expr3Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Expr3Context,i)


        def OP2(self):
            return self.getToken(BKOOLParser.OP2, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)




    def expr2(self):

        localctx = BKOOLParser.Expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expr2)
        try:
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.expr3()
                self.state = 328
                self.match(BKOOLParser.OP2)
                self.state = 329
                self.expr3()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
                self.expr3()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Expr4Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Expr4Context,i)


        def OP3(self):
            return self.getToken(BKOOLParser.OP3, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)




    def expr3(self):

        localctx = BKOOLParser.Expr3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expr3)
        try:
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.expr4(0)
                self.state = 335
                self.match(BKOOLParser.OP3)
                self.state = 336
                self.expr4(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
                self.expr4(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(BKOOLParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(BKOOLParser.Expr4Context,0)


        def OP4(self):
            return self.getToken(BKOOLParser.OP4, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expr4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 349
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 344
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 345
                    self.match(BKOOLParser.OP4)
                    self.state = 346
                    self.expr5() 
                self.state = 351
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKOOLParser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(BKOOLParser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(BKOOLParser.Expr6Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = BKOOLParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expr5)
        try:
            self.state = 355
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.match(BKOOLParser.NOT)
                self.state = 353
                self.expr5()
                pass
            elif token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.OP0, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.expr6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(BKOOLParser.Expr7Context,0)


        def expr6(self):
            return self.getTypedRuleContext(BKOOLParser.Expr6Context,0)


        def CONCAT(self):
            return self.getToken(BKOOLParser.CONCAT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 365
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                    self.state = 360
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 361
                    self.match(BKOOLParser.CONCAT)
                    self.state = 362
                    self.expr7() 
                self.state = 367
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(BKOOLParser.Expr8Context,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = BKOOLParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expr7)
        try:
            self.state = 374
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.expr8(0)
                self.state = 369
                self.match(BKOOLParser.LSB)
                self.state = 370
                self.expr(0)
                self.state = 371
                self.match(BKOOLParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 373
                self.expr8(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(BKOOLParser.Expr9Context,0)


        def expr8(self):
            return self.getTypedRuleContext(BKOOLParser.Expr8Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(BKOOLParser.ExprlistContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 391
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 389
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 379
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 380
                        self.match(BKOOLParser.DOT)
                        self.state = 381
                        self.match(BKOOLParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Expr8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                        self.state = 382
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 383
                        self.match(BKOOLParser.DOT)
                        self.state = 384
                        self.match(BKOOLParser.ID)
                        self.state = 385
                        self.match(BKOOLParser.LB)
                        self.state = 386
                        self.exprlist()
                        self.state = 387
                        self.match(BKOOLParser.RB)
                        pass

             
                self.state = 393
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(BKOOLParser.NEW, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(BKOOLParser.ExprlistContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def expr10(self):
            return self.getTypedRuleContext(BKOOLParser.Expr10Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)




    def expr9(self):

        localctx = BKOOLParser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expr9)
        try:
            self.state = 401
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.match(BKOOLParser.NEW)
                self.state = 395
                self.match(BKOOLParser.ID)
                self.state = 396
                self.match(BKOOLParser.LB)
                self.state = 397
                self.exprlist()
                self.state = 398
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.OP0, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
                self.expr10()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def exprlist(self):
            return self.getTypedRuleContext(BKOOLParser.ExprlistContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def expr11(self):
            return self.getTypedRuleContext(BKOOLParser.Expr11Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr10" ):
                return visitor.visitExpr10(self)
            else:
                return visitor.visitChildren(self)




    def expr10(self):

        localctx = BKOOLParser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expr10)
        try:
            self.state = 408
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 403
                self.match(BKOOLParser.LP)
                self.state = 404
                self.exprlist()
                self.state = 405
                self.match(BKOOLParser.RP)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.OP0, BKOOLParser.LB, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
                self.expr11()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def expr12(self):
            return self.getTypedRuleContext(BKOOLParser.Expr12Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr11" ):
                return visitor.visitExpr11(self)
            else:
                return visitor.visitChildren(self)




    def expr11(self):

        localctx = BKOOLParser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expr11)
        try:
            self.state = 415
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 410
                self.match(BKOOLParser.LB)
                self.state = 411
                self.expr(0)
                self.state = 412
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.OP0, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 414
                self.expr12()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr12Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP0(self):
            return self.getToken(BKOOLParser.OP0, 0)

        def expr12(self):
            return self.getTypedRuleContext(BKOOLParser.Expr12Context,0)


        def operands(self):
            return self.getTypedRuleContext(BKOOLParser.OperandsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr12

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr12" ):
                return visitor.visitExpr12(self)
            else:
                return visitor.visitChildren(self)




    def expr12(self):

        localctx = BKOOLParser.Expr12Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expr12)
        try:
            self.state = 420
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.OP0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 417
                self.match(BKOOLParser.OP0)
                self.state = 418
                self.expr12()
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 419
                self.operands()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def TRUE(self):
            return self.getToken(BKOOLParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKOOLParser.FALSE, 0)

        def NIL(self):
            return self.getToken(BKOOLParser.NIL, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def STRLIT(self):
            return self.getToken(BKOOLParser.STRLIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = BKOOLParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_operands)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.NIL) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.INTLIT) | (1 << BKOOLParser.FLOATLIT) | (1 << BKOOLParser.STRLIT) | (1 << BKOOLParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def argumentslist(self):
            return self.getTypedRuleContext(BKOOLParser.ArgumentslistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = BKOOLParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_exprlist)
        try:
            self.state = 428
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW, BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NIL, BKOOLParser.THIS, BKOOLParser.OP0, BKOOLParser.NOT, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.STRLIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self.expr(0)
                self.state = 425
                self.argumentslist()
                pass
            elif token in [BKOOLParser.RB, BKOOLParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldaccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def exprlist(self):
            return self.getTypedRuleContext(BKOOLParser.ExprlistContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_fieldaccess

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldaccess" ):
                return visitor.visitFieldaccess(self)
            else:
                return visitor.visitChildren(self)




    def fieldaccess(self):

        localctx = BKOOLParser.FieldaccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_fieldaccess)
        try:
            self.state = 451
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                self.expr(0)
                self.state = 431
                self.match(BKOOLParser.DOT)
                self.state = 432
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 434
                self.expr(0)
                self.state = 435
                self.match(BKOOLParser.DOT)
                self.state = 436
                self.match(BKOOLParser.ID)
                self.state = 437
                self.match(BKOOLParser.LB)
                self.state = 438
                self.exprlist()
                self.state = 439
                self.match(BKOOLParser.RB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 441
                self.match(BKOOLParser.ID)
                self.state = 442
                self.match(BKOOLParser.DOT)
                self.state = 443
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 444
                self.match(BKOOLParser.ID)
                self.state = 445
                self.match(BKOOLParser.DOT)
                self.state = 446
                self.match(BKOOLParser.ID)
                self.state = 447
                self.match(BKOOLParser.LB)
                self.state = 448
                self.exprlist()
                self.state = 449
                self.match(BKOOLParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentslistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def argumentslist(self):
            return self.getTypedRuleContext(BKOOLParser.ArgumentslistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_argumentslist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentslist" ):
                return visitor.visitArgumentslist(self)
            else:
                return visitor.visitChildren(self)




    def argumentslist(self):

        localctx = BKOOLParser.ArgumentslistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_argumentslist)
        try:
            self.state = 458
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 453
                self.match(BKOOLParser.COMMA)
                self.state = 454
                self.expr(0)
                self.state = 455
                self.argumentslist()
                pass
            elif token in [BKOOLParser.RB, BKOOLParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarvarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_scalarvar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalarvar" ):
                return visitor.visitScalarvar(self)
            else:
                return visitor.visitChildren(self)




    def scalarvar(self):

        localctx = BKOOLParser.ScalarvarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_scalarvar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def arraycell(self):
            return self.getTypedRuleContext(BKOOLParser.ArraycellContext,0)


        def fieldaccess(self):
            return self.getTypedRuleContext(BKOOLParser.FieldaccessContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_lhs)
        try:
            self.state = 465
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 463
                self.arraycell()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 464
                self.fieldaccess()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraycellContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arraycell

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraycell" ):
                return visitor.visitArraycell(self)
            else:
                return visitor.visitChildren(self)




    def arraycell(self):

        localctx = BKOOLParser.ArraycellContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_arraycell)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            self.expr(0)
            self.state = 468
            self.match(BKOOLParser.LSB)
            self.state = 469
            self.expr(0)
            self.state = 470
            self.match(BKOOLParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraytypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arraytype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraytype" ):
                return visitor.visitArraytype(self)
            else:
                return visitor.visitChildren(self)




    def arraytype(self):

        localctx = BKOOLParser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_arraytype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 472
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 473
            self.match(BKOOLParser.LSB)
            self.state = 474
            self.match(BKOOLParser.INTLIT)
            self.state = 475
            self.match(BKOOLParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[30] = self.expr_sempred
        self._predicates[31] = self.expr1_sempred
        self._predicates[34] = self.expr4_sempred
        self._predicates[36] = self.expr6_sempred
        self._predicates[38] = self.expr8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr6_sempred(self, localctx:Expr6Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr8_sempred(self, localctx:Expr8Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




