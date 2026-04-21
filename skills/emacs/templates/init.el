;;; init.el — MOO Emacs bootstrap (copy tree to ~/.emacs.d/moo/)

(let ((moo-dir (expand-file-name "moo" user-emacs-directory)))
  (add-to-list 'load-path (expand-file-name "lib" moo-dir))
  (dolist (f '("moo-protocol" "moo-structural" "moo-oneshot" "moo-macros"))
    (load f t t)))

(provide 'moo-init)
