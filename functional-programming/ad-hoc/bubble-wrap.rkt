;; Bubble wrap has dimensions NxM, i.e. it has N rows and each row has M cells
;; which has a bubble. Initially all bubbles in filled with air and can be
;; popped.
;;
;; Randomly pick one cell and try to pop it. There might be a case that the
;; bubble is already popped. Both of these steps take 1 second of time. Tell
;; the total expected number of seconds to pop them all.
;;
;; Input: 
;; Input contains a single line containing two space seperated integers, N M,
;; representing the dimension of Bubble wrap.
;;
;; Output: 
;; Output the required answer in one line.

#lang racket

(define (harmonic-sum n)
  (let ((gamma 0.57721566490153286060651209008240243104215933593992))
    ;; gamma + log(n) + 0.5/n - 1./(12*n**2) + 1./(120*n**4)
    (+ (- (+ (+ gamma (log n))
             (/ 0.5 n))
          (/ 1 (* 12 (expt n 2))))
       (/ 1 (* 120 (expt n 4))))))

(define (solve n)
  (real->decimal-string 
    (* n (harmonic-sum n))
    9))

(display (solve (* (read) (read))))
