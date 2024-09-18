
import json

def main():
    p_dict = {
        "이름": "홍길동",        
        "나이": "29",        
        "거주지": "안산시",        
        "신체정보": {
            "키"    : 175.4,
            "몸무게": 71.2,
        },        
        "취미": ["등산", "자전거타기", "독서"]
    }
    print(type(p_dict))

    # Convert to Json string
    j_dict = json.dumps(p_dict, indent=3, sort_keys=True, ensure_ascii=False)
    print(type(j_dict))
    print(j_dict)

    # Convert back to python dict(Default Data Structure)
    p_dict2 = json.loads(j_dict)
    print(type(p_dict2))
    print(p_dict2)


if __name__=="__main__":
    print("Execute main function")
    main()
    print("Fisnish main function")

