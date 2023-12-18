import tkinter as tk
import numpy as np
import signal_plot
import math


def determine_window_type(stop_band):
    stop_band = int(stop_band)
    window_type = {
        21: 'rectangular',
        44: 'hanning',
        53: 'hamming',
        74: 'blackman'
    }

    print(window_type.items)
    print(f'filter specifications keys {window_type.keys}')
    # for band in window_type.keys():
    #     if stop_band >= band:
    #         return window_type[band]
    nearest_key = min(key for key in window_type if key >= stop_band)
    return window_type[nearest_key]


def determine_filter_type(filter_type_from_file):
    return filter_type_from_file


def get_N(norm_fc, window_type):
    def handle_N(N):
        if (N % 2 == 0):
            return np.ceil(N) + 1
        else:
            return np.ceil(N)

    if (window_type == 'rectangular'):
        return handle_N((0.9 / norm_fc))
    elif window_type == 'hanning':
        return handle_N((3.1 / norm_fc))
    elif window_type == 'hamming':
        return handle_N((3.3 / norm_fc))
    elif window_type == 'blackman':
        return handle_N((5.5 / norm_fc))


filter_specs = signal_plot.read_filter_specifications()
print(f'filter_specs: {filter_specs}')

window_type = determine_window_type(filter_specs['StopBandAttenuation '])
print(f'window_type {window_type}')

normalized_transition_band_delta_f = int(filter_specs['TransitionBand ']) / int(filter_specs['FS '])
print(f'normalized_fc {normalized_transition_band_delta_f}')

N = get_N(norm_fc=normalized_transition_band_delta_f, window_type=window_type)
print(f'N: {N}')


def get_fc_dash(filter_specs):
    if (filter_specs['FilterType '].__contains__('Low pass')):
        return (int(filter_specs['FC ']) + (int(filter_specs['TransitionBand ']) / 2)) / int(filter_specs['FS ']), None
    elif filter_specs['FilterType '].__contains__('High pass'):
        return (int(filter_specs['FC ']) - (int(filter_specs['TransitionBand ']) / 2)) / int(filter_specs['FS ']), None
    elif filter_specs['FilterType '].__contains__('Band pass'):
        return (int(filter_specs['F1 ']) - (int(filter_specs['TransitionBand ']) / 2)) / int(filter_specs['FS ']), (
                    int(filter_specs['F2 ']) + (int(filter_specs['TransitionBand ']) / 2)) / int(filter_specs['FS '])
    else:
        return (int(filter_specs['F1 ']) + (int(filter_specs['TransitionBand ']) / 2)) / int(filter_specs['FS ']), (
                    int(filter_specs['F2 ']) - (int(filter_specs['TransitionBand ']) / 2)) / int(filter_specs['FS '])


def truncate_signal(N):
    list_1 = []
    list_2 = []
    for i in range((N / 2).__ceil__()):
        list_1.append(i)
        list_2.append(-i)
    indicates = list_1 + list_2
    indicates = list(set(indicates))
    indicates.sort()
    return indicates


def fill_window_list(window_type, N):
    truncated_signal_elements = []
    for element in range(np.ceil(N / 2)):
        if (window_type == 'hanning'):
            truncated_signal_elements.append(apply_hanning_window_fnc(element, N))
        elif window_type == 'hamming':
            truncated_signal_elements.append(apply_hamming_window_fnc(element, N))
        elif window_type == 'blackman':
            truncated_signal_elements.append(apply_blackman_window_fnc(element, N))
        else:
            return truncated_signal_elements


def apply_hanning_window_fnc(element, N):
    return 0.5 + (0.5 * (math.cos((2 * np.pi * element) / N)))


def apply_hamming_window_fnc(element, N):
    return 0.54 + (0.46 * (math.cos((2 * np.pi * element) / N)))


def apply_blackman_window_fnc(element, N):
    return 0.42 + (0.08 * math.cos((4 * np.pi * element) / (N - 1))) + (
    (0.5 * (math.cos((2 * np.pi * element) / (N - 1)))))


def get_filtered_elements(filter_type, n, f1, f2):
    filtered_list = []

    if filter_type.__contains__('Low pass'):
        for element in range((n / 2).__ceil__()):
            if element == 0:
                filtered_list.append(2 * f1)
            else:
                tmp = element * 2 * math.pi * f1
                filtered_list.append(2 * f1 * (math.sin(tmp) / tmp))
    elif filter_type.__contains__('High pass'):
        for element in range((n / 2).__ceil__()):
            if element == 0:
                filtered_list.append(1 - (2 * f1))
            else:
                tmp = element * 2 * math.pi * f1
                filtered_list.append(-2 * f1 * (math.sin(tmp) / tmp))
    elif filter_type.__contains__('Band pass'):
        for element in range((n / 2).__ceil__()):
            if element == 0:
                filtered_list.append(2 * round(f2 - f1, 2))
            else:
                tmp1 = element * 2 * math.pi * f1
                tmp2 = element * 2 * math.pi * f2
                filtered_list.append(
                    (2 * f2 * (math.sin(tmp2) / tmp2)) - (
                                2 * f1 * (math.sin(tmp1) / tmp1)))
    elif filter_type.__contains__('Band pass'):
        for element in range((n / 2).__ceil__()):
            if element == 0:
                filtered_list.append(1 - (2 * (f2 - f1)))
            else:
                x1 = element * 2 * math.pi * f1
                x2 = element * 2 * math.pi * f2
                filtered_list.append(((2 * f2 * (math.sin(x2) / x2)) - (2 * f1 * (math.sin(x1) / x1))) * -1)

    return filtered_list


def fill_filtered_list(window_list, filtered_list):
    list1 = [x * y for x, y in zip(window_list, filtered_list)]
    list2 = [x * y for x, y in zip(window_list, filtered_list)]
    list2.reverse()
    list2.extend(list1)
    list2.remove(list2[int(len(list2) / 2)])
    return list2


def apply_filter(filter_specs):
    window_type = determine_window_type(filter_specs['StopBandAttenuation '])
    normalized_transition_band_delta_f = int(filter_specs['TransitionBand ']) / int(filter_specs['FS '])
    N = get_N(normalized_transition_band_delta_f, window_type)
    (f1, f2) = get_fc_dash(filter_specs)
    window_elements = truncate_signal(N)
    _filtered_elements = fill_filtered_list(window_elements,
                                            get_filtered_elements(filter_specs['FilterType '], N, f1, f2))
    print(len(_filtered_elements))
    return window_elements, _filtered_elements


def down_sampling(window_elements, signal, factor_m):
    sampled_signal = []
    sampled_signal_indecies = []

    for i in range(0, len(signal), factor_m):
        sampled_signal.append(signal[i])

    for i in range(len(sampled_signal)):
        sampled_signal_indecies.append(window_elements[i])

    return sampled_signal, sampled_signal_indecies


def up_sampling(window_elements, signal, factor_l):
    sampled_signal = []
    sampled_signal_indecies = []

    for i in range(len(window_elements)):
        sampled_signal.append(signal[i])
        for _ in range(factor_l - 1):
            sampled_signal.append(0)

    for i in range(len(sampled_signal)):
        sampled_signal_indecies.append(i)

    return sampled_signal_indecies, sampled_signal


def convolve_signals(window_elements, calculated_filtered_signal, window_elements_2, signal_2):
    min_ind = int(window_elements[0] + window_elements_2[0])
    max_ind = int(window_elements[-1] + window_elements_2[-1])
    result_length = max_ind - min_ind + 1

    result = [0] * result_length
    indices = [i for i in range(min_ind, max_ind + 1)]

    for i in range(len(window_elements)):
        for j in range(len(window_elements_2)):
            index = int(window_elements[i] + window_elements_2[j])
            result[index - min_ind] += calculated_filtered_signal[i] * signal_2[j]
    return indices, result


def resampling(factor_m, factor_l):
    window_elements, filtered_elements = apply_filter(filter_specs)
    _, _, _, signal_elements, signal = read_signal_ecg_file()
    if factor_l == 0 and factor_m != 0:
        x, y = apply_filter(filter_specs)
        return down_sampling(x, y, factor_m)
    elif factor_l == 0 and factor_m != 0:
        m, n = perform_up_sampling(
            signal_elements, signal, factor_l, window_elements, filtered_elements,
        )
        return m, n
    elif factor_l != 0 and factor_m != 0:
        t, p = up_sampling(signal_elements, signal, factor_l)
        x, y = convolve_signals(signal_elements, filtered_elements, t, p, )
        m, n = down_sampling(x, y, factor_m)

        n.remove(n[-1])
        m.remove(m[-1])
        return m, n

    return None, None


def perform_up_sampling(signal_elements, signal, factor_l, window_elements, filtered_elements, ):
    # Applying upsamling to the filter output
    signal_elements, signal = up_sampling(signal_elements, signal, factor_l=factor_l)
    m, n = convolve_signals(window_elements, filtered_elements, signal_elements, signal)
    for i in range(2):
        n.remove(n[-1])
        m.remove(m[-1])

    return m, n


def read_signal_ecg_file():
    # signal_type, is_periodic, num_samples, indexes, values =
    return signal_plot.read_signal_ecg_file()
