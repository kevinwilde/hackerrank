#lang racket

;; You are given two integer arrays, A and B, each containing N integers.
;; Is there an permutation A', B' possible of A and B, such that, A'i+B'i ≥ K
;; for all i, where A'i denotes the ith element in the array A' and B'i denotes
;; the ith element in the array B'.
;;
;; Input Format
;; The first line contains an integer, T, the number of test-cases. T test cases
;; follow. Each test case has the following format:
;;
;; The first line contains two integers, N and K. The second line contains N
;; space separated integers, denoting array A. The third line describes array B
;; in a same format.
;;
;; Output Format
;; For each test case, if such an arrangement exists, output "YES", otherwise
;; "NO" (without quotes).

(define (read-list)
  (map string->number (string-split (read-line))))

(define (zip lst1 lst2)
  (map list lst1 lst2))

(define (element-wise-add lst1 lst2)
  (map (lambda (pair) (foldl + 0 pair)) (zip lst1 lst2)))

(define (solve K lst1 lst2)
  (let ([lst1 (sort lst1 <)]
        [lst2 (sort lst2 >)])
    (empty? (filter (lambda (x) (< x K)) (element-wise-add lst1 lst2)))))

(let ([T (read)])
  (for ([_ T])
       (let ([N (read)]
             [K (read)]
             [_ (read-line)]
             [a (read-list)]
             [b (read-list)])
         (if (not (and (equal? N (length a))
                       (equal? N (length b))))
             (error 'input "arrays not equal length")
             (if (solve K a b)
                 (printf "YES\n")
                 (printf "NO\n"))))))

;; Unit Tests
(require rackunit)
(check-equal? (zip (list 1 2 3) (list 4 5 6))
              (list (list 1 4) (list 2 5) (list 3 6)))
(check-equal? (element-wise-add (list 1 2 3) (list 4 5 6))
              (list 5 7 9))
(check-true (solve 5 '(1 2 3) '(2 3 4)))
(check-false (solve 6 '(1 2 3) '(2 3 4)))
