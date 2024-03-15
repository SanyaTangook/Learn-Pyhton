def rearrange_array(arr):
    frequency_map = {}
    
    # นับความถี่ของแต่ละตัวเลขในอาร์เรย์
    for num in arr:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1
    
    # เรียงลำดับตัวเลขตามความถี่ และตามค่า
    sorted_nums = sorted(frequency_map.items(), key=lambda x: (-x[1], x[0]))
    
    result = []
    for num, freq in sorted_nums:
        result.extend([num] * freq)
    
    return frequency_map
# รับ input array จากผู้ใช้
input_array = list(map(int, input("Input: ").split()))

# เรียกใช้ฟังก์ชันและแสดง output array
output_array = rearrange_array(input_array)
print("Output:", output_array)
