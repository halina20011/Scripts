local fn = vim.fn

-- Automatically install packer
local install_path = fn.stdpath "data" .. "/site/pack/packer/start/packer.nvim"
if fn.empty(fn.glob(install_path)) > 0 then
	PACKER_BOOTSTRAP = fn.system {
        "git",
        "clone",
        "--depth",
        "1",
        "https://github.com/wbthomason/packer.nvim",
        install_path,
	}
	print "Installing packer close and reopen Neovim..."
	vim.cmd [[packadd packer.nvim]]
end

-- Autocommand that reloads neovim whenever you save the plugins.lua file
vim.cmd [[
    augroup packer_user_config
    autocmd!
    autocmd BufWritePost plugins.lua source <afile> | PackerSync
    augroup end
]]

-- Use a protected call so we don't error out on first use
local status_ok, packer = pcall(require, "packer")
if not status_ok then
    return
end

-- Have packer use a popup window
packer.init({
	display = {
		open_fn = function()
			return require("packer.util").float({ border = "rounded" })
		end,
	},
})

-- Install your plugins here
return packer.startup(function(use)
    use { "wbthomason/packer.nvim", commit = "6afb67460283f0e990d35d229fd38fdc04063e0a" } -- have packer manage itself
    use "nvim-lua/popup.nvim" -- an implementation of the Popup API from vim in Neovim
    use "nvim-lua/plenary.nvim" -- useful lua functions used ny lots of plugins
    use "folke/which-key.nvim"
    -- Indent Blankline
    use "lukas-reineke/indent-blankline.nvim"

    -- Colorschemes
    -- use "lunarvim/colorschemes" -- A bunch of colorschemes you can try out
    use "folke/tokyonight.nvim"
    --use "lunarvim/darkplus.nvim"

    -- cmp plugins
    use "hrsh7th/nvim-cmp"              -- The completion plugin
    use "hrsh7th/cmp-buffer"            -- buffer completions
    use "hrsh7th/cmp-path"              -- path completions
    use "hrsh7th/cmp-cmdline"           -- cmdline completions
    use "saadparwaiz1/cmp_luasnip"      -- snippet completions
    use "hrsh7th/cmp-nvim-lsp"
    use "hrsh7th/cmp-nvim-lua"

    -- Snippets
    use "L3MON4D3/LuaSnip" -- Snippet engine
    use "rafamadriz/friendly-snippets" -- a bunch of snippets to use

    -- LSP
    use { "neovim/nvim-lspconfig", commit = "f11fdff7e8b5b415e5ef1837bdcdd37ea6764dda" }
    -- simple to use language server installer
    use { "williamboman/mason.nvim", commit = "c2002d7a6b5a72ba02388548cfaf420b864fbc12"} 
    use { "williamboman/mason-lspconfig.nvim", commit = "0051870dd728f4988110a1b2d47f4a4510213e31" }
    -- for formatters and linters
    use { "jose-elias-alvarez/null-ls.nvim", commit = "c0c19f32b614b3921e17886c541c13a72748d450" } 
    
    -- nvim-treesitter
    -- https://github.com/nvim-treesitter/nvim-treesitter
    use { "nvim-treesitter/nvim-treesitter", run = ":TSUpdate",}
    use "nvim-treesitter/playground"

    -- Git
    use "lewis6991/gitsigns.nvim"

    -- Comment
    use "numToStr/Comment.nvim"
    
    -- Latex
    use "lervag/vimtex"

    -- Automatically set up your configuration after cloning packer.nvim
    -- Put this at the end after all plugins
    if PACKER_BOOTSTRAP then
        require("packer").sync()
    end
end)
