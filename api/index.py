from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

SINGLE_SURNAMES = list("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康伍余元卜顾孟平黄和穆萧尹姚邵湛汪祁毛禹狄米贝明")
COMPOUND_SURNAMES = ["欧阳", "司马", "上官", "诸葛", "东方", "皇甫", "令狐", "公孙", "慕容", "南宫", "夏侯", "宇文"]

MALE_GIVEN = list("子轩浩然宇辰博文景行承泽俊熙睿航奕辰泽宇明哲")
FEMALE_GIVEN = list("梓涵诗雨若溪语彤可欣依诺静妍沐瑶芷晴星妍")
NEUTRAL_GIVEN = list("安宁清和知远云舟星河言初见山若水简宁")

PAIR_MALE = ["浩然", "景行", "承泽", "明轩", "修远", "泽宇", "子墨", "星野"]
PAIR_FEMALE = ["若溪", "语彤", "静妍", "沐瑶", "芷晴", "星妍", "可心", "知夏"]
PAIR_NEUTRAL = ["清和", "知远", "云舟", "若水", "见山", "言初", "安宁", "简宁"]


def pick_gender_pool(gender: str):
    if gender == "male":
        return MALE_GIVEN, PAIR_MALE
    if gender == "female":
        return FEMALE_GIVEN, PAIR_FEMALE
    if gender == "neutral":
        return NEUTRAL_GIVEN, PAIR_NEUTRAL
    return MALE_GIVEN + FEMALE_GIVEN + NEUTRAL_GIVEN, PAIR_MALE + PAIR_FEMALE + PAIR_NEUTRAL


@app.get("/api/health")
def health():
    return jsonify({"ok": True})


@app.get("/api/generate")
def generate_name():
    gender = request.args.get("gender", "random")
    surname_type = request.args.get("surnameType", "single")
    given_type = request.args.get("givenType", "double")

    if surname_type == "compound":
        surname = random.choice(COMPOUND_SURNAMES)
    else:
        surname = random.choice(SINGLE_SURNAMES)

    chars, pairs = pick_gender_pool(gender)

    if given_type == "single":
        given = random.choice(chars)
    else:
        given = random.choice(pairs)

    return jsonify({"name": f"{surname}{given}"})
