�
    ���d8  �                   �0  � d dl Z d dlZd dlZd dlZd dlmZ g ZdZdZ e j	        e�  �        D ]�Z
e
�                    d�  �        s�e j        �                    ee
�  �        Z eed�  �        5 Ze�                    �   �         Z eed�  �        Ze�                    d�  �        j        Ze�                    e�  �         ddd�  �         n# 1 swxY w Y   �� ej        d	d
d� eD �   �         ��  �        gZ ej        e�  �        Zed	         Z ej        ddg d���  �        gZ ej        e�  �        Zed         Zedk    r� ej         ededg�  �          ej!        ddd��  �        gZ" ej        e"�  �        Z#e#d         du r= e$d�  �          ej         ddgej%        ��  �        Z& e$de&�  �          e$d�  �         dS  e$d�  �          e$d�  �         dS edk    r ej         edeg�  �         dS edk    r ej         edeg�  �         dS  e$d �  �         dS )!�    N)�BeautifulSoupzDc:\ProgramData\Cisco\Cisco AnyConnect Secure Mobility Client\ProfilezOc:\Program Files (x86)\Cisco\Cisco AnyConnect Secure Mobility Client\vpncli.exez.xml�r�xml�HostName�ConnectionTypezSelect a connection:c                 �   � g | ]}|��S � r	   )�.0�
connections     �AnyConnect-Windows.py�
<listcomp>r   -   s   � �Q�Q�Q�
��Q�Q�Q�    )�message�choices�
ActionTypezSelect an action:)�connect�
disconnect�statusr   z-s�
MetricEditzDDo you want to set the Cisco AnyConnect adapter metric to value 100?T)r   �defaultzYou choosed Yes.�
powershellz~Get-NetAdapter | Where-Object { $_.InterfaceDescription -like '*Cisco AnyConnect*' } | Set-NetIPInterface -InterfaceMetric 100)�stdoutzResult: z6AnyConnect-Windows python script is telling goodbye :)zYou choosed Noz5AnyConnect-Windows python script is telling goodbye:)r   r   z<The action choice selected doesn't exist. Contact developer.)'�os�inquirer�
subprocess�sys�bs4r   �ListOfAvailableConnections�AnyConnectProfilesPath�AnyConnectVpnCli�listdir�filename�endswith�path�join�fullname�open�f�read�data�Bs_data�find�string�Hostname�append�List�HostNameQuestions�prompt�HostNameAnswers�HostNameAnswer�ActionQuestions�ActionAnswers�ActionAnswer�run�Confirm�NetAdapterMetricQuestion�NetAdapterMetricAnswer�printr   �cr	   r   r   �<module>r>      sn  �� 
�	�	�	� ���� � � � � 
�
�
�
� � � � � � �  � �_� �h� � ��
�1�2�2� 4� 4�H����V�$�$�.�h��w�|�|�2�H�=�=�H� 
��h��	�	� 	4���v�v�x�x���-��e�,�,���<�<�
�+�+�2�� 	#�)�)�(�3�3�3�	4� 	4� 	4� 	4� 	4� 	4� 	4� 	4� 	4� 	4� 	4���� 	4� 	4� 	4� 	4�� �H�M�"�.�Q�Q�6P�Q�Q�Q�� � �� � "�(�/�"3�4�4�� �!1�2�� �H�M�,�+�;�;�;�� � ���  ����0�0���\�*���9����J�N�$�j�.�%�H�I�I�I� �H��\�+q�{�  A�  A�  A� �� -�X�_�-E�F�F���l�+�t�3�3��� �!�!�!��J�N�L�  +k�  l�  ux�  u�  @�  @�  @����z�1������F�G�G�G�G�G���������E�F�F�F�F�F��\�!�!��J�N�$�m�^�D�E�E�E�E�E��X����J�N�$�i��@�A�A�A�A�A� 
�E�
H�I�I�I�I�Is   �,AC�C	�C	