import cv2
import numpy as np
from scipy.signal import convolve2d

def lucy_richardson(image, psf, iterations):
    img = image.astype(np.float64)
    estimate = img.copy()
    for _ in range(iterations):
        relative_blur = img / (convolve2d(estimate, psf, 'same') + 1e-7)
        estimate *= convolve2d(relative_blur, psf[::-1, ::-1], 'same')
    return estimate

def enhance_edges(image):
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    edge_enhanced = cv2.magnitude(sobel_x, sobel_y)
    return edge_enhanced

def upscale_image(image, scale=2):
    # OpenCV의 DNN Super Resolution 모델 사용
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel("D:/GitHub/Python/HdChemeng/Image/EDSR_x2.pb")  # EDSR 모델 파일 경로 필요
    sr.setModel("edsr", scale)  # "edsr" 모델로 설정 및 업스케일링 비율
    return sr.upsample(image)

def deblur_image(image_path, output_path):
    # 이미지 읽기
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("이미지를 찾을 수 없습니다.")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # PSF 정의 (점 확산 함수)
    psf = np.ones((5, 5)) / 25
    restored = np.zeros_like(image)
    
    # 각 채널에 대해 루시-리처드슨 적용 및 에지 강화
    for i in range(3):
        restored_channel = lucy_richardson(image[:, :, i], psf, iterations=10)
        edges = enhance_edges(image[:, :, i])
        restored[:, :, i] = cv2.addWeighted(restored_channel, 0.7, edges, 0.3, 0)

    # 해상도 업스케일링
    restored_upscaled = upscale_image(np.clip(restored, 0, 255).astype(np.uint8))

    # 저장하기
    restored_bgr = cv2.cvtColor(restored_upscaled, cv2.COLOR_RGB2BGR)
    cv2.imwrite(output_path, restored_bgr)
    print(f"Deblurred and upscaled image saved at {output_path}")

# 예시: 이미지 경로 및 저장 경로 지정 후 호출
deblur_image(
    'D:/GitHub/Python/HdChemeng/Image/blurred_image.png', 
    'D:/GitHub/Python/HdChemeng/Image/deblurred_image.png'
)
